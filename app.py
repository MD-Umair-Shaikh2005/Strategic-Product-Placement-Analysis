"""
Flask Application for Strategic Product Placement Analysis
Main application entry point
"""

from flask import Flask, render_template, jsonify, request
import os
import pandas as pd
from config import config
from scripts.data_preparation import DataProcessor
from scripts.visualizations import VisualizationManager


def create_app(config_name='development'):
    """Application factory"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize global variables
    app.data_processor = None
    app.viz_manager = None
    app.dataset_loaded = False
    
    @app.before_request
    def load_dataset():
        """Load dataset before first request"""
        if not app.dataset_loaded:
            dataset_path = app.config['DATASET_PATH']
            if os.path.exists(dataset_path):
                try:
                    app.data_processor = DataProcessor(dataset_path)
                    app.data_processor.load_data()
                    app.data_processor.clean_data()
                    app.viz_manager = VisualizationManager(app.data_processor.get_processed_data())
                    app.dataset_loaded = True
                    print("✓ Dataset loaded and processed successfully")
                except Exception as e:
                    print(f"✗ Error loading dataset: {str(e)}")
    
    # ==================== ROUTES ====================
    
    @app.route('/')
    def index():
        """Home page"""
        return render_template('index.html', dataset_loaded=app.dataset_loaded)
    
    @app.route('/dashboard')
    def dashboard():
        """Main dashboard with all visualizations"""
        if not app.dataset_loaded:
            return render_template('error.html', message="Dataset not loaded. Please upload a CSV file."), 400
        
        try:
            # Get data statistics
            stats = app.data_processor.generate_statistics()
            
            # Get visualizations
            visualizations = app.viz_manager.get_all_visualizations()
            
            return render_template('dashboard.html', 
                                 visualizations=visualizations,
                                 stats=stats)
        except Exception as e:
            return render_template('error.html', message=f"Error loading dashboard: {str(e)}"), 500
    
    @app.route('/api/data-info')
    def data_info():
        """API endpoint for data information"""
        if not app.dataset_loaded:
            return jsonify({'error': 'Dataset not loaded'}), 400
        
        try:
            info = app.data_processor.get_data_info()
            return jsonify(info)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @app.route('/api/statistics')
    def statistics():
        """API endpoint for data statistics"""
        if not app.dataset_loaded:
            return jsonify({'error': 'Dataset not loaded'}), 400
        
        try:
            stats = app.data_processor.generate_statistics()
            return jsonify(stats)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @app.route('/api/visualization/<viz_name>')
    def get_visualization(viz_name):
        """API endpoint for specific visualization"""
        if not app.dataset_loaded:
            return jsonify({'error': 'Dataset not loaded'}), 400
        
        try:
            all_viz = app.viz_manager.get_all_visualizations()
            if viz_name in all_viz:
                return all_viz[viz_name], 200, {'Content-Type': 'application/json'}
            else:
                return jsonify({'error': f'Visualization {viz_name} not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @app.route('/upload', methods=['POST'])
    def upload_file():
        """Handle CSV file upload"""
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.csv'):
            return jsonify({'error': 'Only CSV files are supported'}), 400
        
        try:
            # Save uploaded file
            upload_dir = app.config['DATA_DIR']
            os.makedirs(upload_dir, exist_ok=True)
            filepath = os.path.join(upload_dir, 'product_placement_data.csv')
            file.save(filepath)
            
            # Process the file
            app.data_processor = DataProcessor(filepath)
            app.data_processor.load_data()
            app.data_processor.clean_data()
            app.viz_manager = VisualizationManager(app.data_processor.get_processed_data())
            app.dataset_loaded = True
            
            info = app.data_processor.get_data_info()
            return jsonify({
                'success': True,
                'message': 'File uploaded and processed successfully',
                'data_info': info
            })
        except Exception as e:
            return jsonify({'error': f'Error processing file: {str(e)}'}), 500
    
    @app.route('/insights')
    def insights():
        """Insights and recommendations page"""
        if not app.dataset_loaded:
            return render_template('error.html', message="Dataset not loaded."), 400
        
        return render_template('insights.html')
    
    @app.route('/story')
    def story():
        """Story/presentation page"""
        if not app.dataset_loaded:
            return render_template('error.html', message="Dataset not loaded."), 400
        
        return render_template('story.html')
    
    # ==================== ERROR HANDLERS ====================
    
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors"""
        return render_template('error.html', message="Page not found."), 404
    
    @app.errorhandler(500)
    def server_error(error):
        """Handle 500 errors"""
        return render_template('error.html', message="Internal server error."), 500
    
    # ==================== CONTEXT PROCESSORS ====================
    
    @app.context_processor
    def inject_config():
        """Inject config variables to templates"""
        return {
            'app_name': 'Product Placement Analysis',
            'app_version': '1.0.0',
            'dataset_loaded': app.dataset_loaded
        }
    
    return app


if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_ENV', 'development'))
    app.run(debug=True, host='0.0.0.0', port=5000)
