"""
Visualization Module
Creates interactive visualizations using Plotly
"""

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import json


class VisualizationManager:
    """Manage all data visualizations"""
    
    def __init__(self, dataframe):
        """Initialize with processed dataframe"""
        self.df = dataframe
        self.colors = px.colors.qualitative.Set2
        
    def sales_by_placement(self):
        """Visualization 1: Sales by Product Placement"""
        if 'Placement' not in self.df.columns or 'Sales' not in self.df.columns:
            return None
            
        sales_by_placement = self.df.groupby('Placement')['Sales'].sum().sort_values(ascending=False)
        
        fig = go.Figure(data=[
            go.Bar(x=sales_by_placement.index, y=sales_by_placement.values, 
                   marker_color=self.colors[0])
        ])
        fig.update_layout(
            title='Total Sales by Product Placement',
            xaxis_title='Placement Location',
            yaxis_title='Sales ($)',
            hovermode='x unified',
            height=500
        )
        return fig
    
    def category_performance(self):
        """Visualization 2: Sales by Category"""
        if 'Category' not in self.df.columns or 'Sales' not in self.df.columns:
            return None
            
        category_sales = self.df.groupby('Category')['Sales'].agg(['sum', 'mean', 'count'])
        
        fig = go.Figure(data=[
            go.Bar(name='Total Sales', x=category_sales.index, y=category_sales['sum'],
                   marker_color=self.colors[1]),
        ])
        fig.update_layout(
            title='Sales Performance by Product Category',
            xaxis_title='Category',
            yaxis_title='Sales ($)',
            height=500
        )
        return fig
    
    def placement_efficiency(self):
        """Visualization 3: Placement Efficiency (Sales per Unit)"""
        if 'Placement' not in self.df.columns or 'Quantity' not in self.df.columns or 'Sales' not in self.df.columns:
            return None
            
        efficiency = self.df.groupby('Placement').apply(
            lambda x: (x['Sales'].sum() / x['Quantity'].sum()) if x['Quantity'].sum() > 0 else 0
        ).sort_values(ascending=False)
        
        fig = go.Figure(data=[
            go.Bar(x=efficiency.index, y=efficiency.values, 
                   marker_color=self.colors[2])
        ])
        fig.update_layout(
            title='Sales Efficiency by Placement (Sales per Unit)',
            xaxis_title='Placement Location',
            yaxis_title='Sales per Unit ($)',
            height=500
        )
        return fig
    
    def sales_trend(self):
        """Visualization 4: Sales Trend Over Time"""
        if 'Date' not in self.df.columns and 'Month' not in self.df.columns:
            # If no temporal data, create a trend visualization
            sales_trend = self.df['Sales'].rolling(window=5).mean()
            fig = go.Figure(data=[
                go.Scatter(y=sales_trend.values, mode='lines', 
                          fill='tozeroy', name='Sales Trend',
                          line_color=self.colors[3])
            ])
        else:
            time_col = 'Date' if 'Date' in self.df.columns else 'Month'
            sales_trend = self.df.groupby(time_col)['Sales'].sum()
            fig = go.Figure(data=[
                go.Scatter(x=sales_trend.index, y=sales_trend.values, mode='lines+markers',
                          fill='tozeroy', name='Sales Over Time',
                          line_color=self.colors[3])
            ])
        
        fig.update_layout(
            title='Sales Trend Analysis',
            xaxis_title='Time Period',
            yaxis_title='Sales ($)',
            hovermode='x unified',
            height=500
        )
        return fig
    
    def customer_demographics(self):
        """Visualization 5: Customer Analysis by Demographics"""
        if 'CustomerAge' not in self.df.columns and 'Region' not in self.df.columns:
            return None
        
        # Try Region if available
        if 'Region' in self.df.columns:
            region_data = self.df.groupby('Region')['Sales'].agg(['sum', 'count'])
            region_data.columns = ['Total Sales', 'Customer Count']
            
            fig = go.Figure(data=[
                go.Bar(name='Total Sales', x=region_data.index, y=region_data['Total Sales'],
                       marker_color=self.colors[4]),
            ])
            fig.update_layout(
                title='Sales by Customer Region',
                xaxis_title='Region',
                yaxis_title='Sales ($)',
                height=500
            )
            return fig
        
        return None
    
    def heatmap_performance(self):
        """Visualization 6: Heatmap of Placement-Category Performance"""
        if 'Placement' not in self.df.columns or 'Category' not in self.df.columns or 'Sales' not in self.df.columns:
            return None
            
        heatmap_data = self.df.pivot_table(values='Sales', index='Placement', 
                                          columns='Category', aggfunc='sum', fill_value=0)
        
        fig = go.Figure(data=go.Heatmap(
            z=heatmap_data.values,
            x=heatmap_data.columns,
            y=heatmap_data.index,
            colorscale='YlOrRd'
        ))
        fig.update_layout(
            title='Sales Heatmap: Placement × Category',
            xaxis_title='Product Category',
            yaxis_title='Placement Location',
            height=500
        )
        return fig
    
    def profit_analysis(self):
        """Visualization 7: Profit by Placement"""
        if 'Placement' not in self.df.columns:
            return None
        
        # If Profit column exists, use it; otherwise calculate from Sales
        if 'Profit' in self.df.columns:
            profit_data = self.df.groupby('Placement')['Profit'].sum().sort_values(ascending=False)
        else:
            profit_data = self.df.groupby('Placement')['Sales'].sum().sort_values(ascending=False) * 0.3  # Assume 30% profit margin
        
        fig = go.Figure(data=[
            go.Bar(x=profit_data.index, y=profit_data.values, 
                   marker_color=self.colors[5])
        ])
        fig.update_layout(
            title='Profit Analysis by Placement',
            xaxis_title='Placement Location',
            yaxis_title='Profit ($)',
            height=500
        )
        return fig
    
    def conversion_analysis(self):
        """Visualization 8: Conversion Metrics"""
        if 'Quantity' not in self.df.columns or 'Sales' not in self.df.columns:
            return None
        
        # Calculate conversion-like metric
        avg_transaction = self.df.groupby('Placement').agg({
            'Sales': 'mean',
            'Quantity': 'mean'
        })
        
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig.add_trace(
            go.Bar(x=avg_transaction.index, y=avg_transaction['Sales'],
                   name='Avg Sales per Transaction', marker_color=self.colors[6]),
            secondary_y=False
        )
        
        fig.add_trace(
            go.Scatter(x=avg_transaction.index, y=avg_transaction['Quantity'],
                      name='Avg Quantity per Transaction', mode='lines+markers',
                      line_color=self.colors[0]),
            secondary_y=True
        )
        
        fig.update_layout(
            title='Transaction Metrics by Placement',
            xaxis_title='Placement Location',
            height=500,
            hovermode='x unified'
        )
        fig.update_yaxes(title_text='Avg Sales ($)', secondary_y=False)
        fig.update_yaxes(title_text='Avg Quantity', secondary_y=True)
        
        return fig
    
    def get_all_visualizations(self):
        """Generate all visualizations as JSON"""
        visualizations = {}
        
        viz_methods = [
            ('sales_by_placement', self.sales_by_placement),
            ('category_performance', self.category_performance),
            ('placement_efficiency', self.placement_efficiency),
            ('sales_trend', self.sales_trend),
            ('customer_demographics', self.customer_demographics),
            ('heatmap_performance', self.heatmap_performance),
            ('profit_analysis', self.profit_analysis),
            ('conversion_analysis', self.conversion_analysis),
        ]
        
        for viz_name, viz_func in viz_methods:
            try:
                fig = viz_func()
                if fig is not None:
                    visualizations[viz_name] = fig.to_json()
            except Exception as e:
                print(f"Error generating {viz_name}: {str(e)}")
        
        return visualizations
