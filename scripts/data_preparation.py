"""
Data Preparation and Cleaning Module
Handles loading, cleaning, and preparing data for analysis
"""

import pandas as pd
import numpy as np
from pathlib import Path


class DataProcessor:
    """Handle data loading, cleaning, and preparation"""
    
    def __init__(self, filepath):
        """Initialize with dataset file path"""
        self.filepath = filepath
        self.df = None
        self.processed_df = None
        
    def load_data(self):
        """Load CSV data"""
        try:
            self.df = pd.read_csv(self.filepath)
            print(f"✓ Dataset loaded successfully. Shape: {self.df.shape}")
            return self.df
        except FileNotFoundError:
            print(f"✗ File not found: {self.filepath}")
            return None
        except Exception as e:
            print(f"✗ Error loading data: {str(e)}")
            return None
    
    def get_data_info(self):
        """Return basic data information"""
        if self.df is None:
            return None
        
        return {
            'shape': self.df.shape,
            'columns': list(self.df.columns),
            'dtypes': self.df.dtypes.to_dict(),
            'missing_values': self.df.isnull().sum().to_dict(),
            'head': self.df.head().to_dict('records')
        }
    
    def clean_data(self):
        """Perform data cleaning"""
        if self.df is None:
            return None
            
        self.processed_df = self.df.copy()
        
        # Remove duplicate rows
        initial_rows = len(self.processed_df)
        self.processed_df = self.processed_df.drop_duplicates()
        removed_duplicates = initial_rows - len(self.processed_df)
        
        # Handle missing values
        missing_info = {}
        for col in self.processed_df.columns:
            missing_count = self.processed_df[col].isnull().sum()
            if missing_count > 0:
                if self.processed_df[col].dtype in ['float64', 'int64']:
                    self.processed_df[col].fillna(self.processed_df[col].median(), inplace=True)
                else:
                    self.processed_df[col].fillna('Unknown', inplace=True)
                missing_info[col] = missing_count
        
        print(f"✓ Data cleaned: Removed {removed_duplicates} duplicates")
        if missing_info:
            print(f"✓ Handled missing values: {missing_info}")
        
        return self.processed_df
    
    def generate_statistics(self):
        """Generate statistical summary"""
        if self.processed_df is None:
            self.clean_data()
            
        stats = {
            'numeric_summary': self.processed_df.describe().to_dict(),
            'categorical_summary': {}
        }
        
        # Categorical summaries
        for col in self.processed_df.select_dtypes(include=['object']).columns:
            stats['categorical_summary'][col] = self.processed_df[col].value_counts().to_dict()
        
        return stats
    
    def get_processed_data(self):
        """Return processed dataframe"""
        if self.processed_df is None:
            self.clean_data()
        return self.processed_df


# Utility functions for quick access
def load_and_process(filepath):
    """Load and process data in one step"""
    processor = DataProcessor(filepath)
    processor.load_data()
    processor.clean_data()
    return processor.get_processed_data()
