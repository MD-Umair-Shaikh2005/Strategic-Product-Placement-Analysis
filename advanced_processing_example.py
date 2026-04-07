#!/usr/bin/env python
"""
Advanced Data Preparation Examples
Additional data cleaning and transformation utilities
"""

import pandas as pd
import numpy as np
from pathlib import Path


class AdvancedDataProcessor:
    """Advanced data processing utilities"""
    
    def __init__(self, df):
        """Initialize with dataframe"""
        self.df = df.copy()
        self.original_df = df.copy()
    
    def handle_outliers_iqr(self, column, multiplier=1.5):
        """Remove outliers using Interquartile Range (IQR)"""
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - multiplier * IQR
        upper_bound = Q3 + multiplier * IQR
        
        removed = len(self.df[(self.df[column] < lower_bound) | (self.df[column] > upper_bound)])
        
        self.df = self.df[(self.df[column] >= lower_bound) & (self.df[column] <= upper_bound)]
        
        print(f"✓ Removed {removed} outliers from {column}")
        return self.df
    
    def normalize_column(self, column):
        """Normalize column to 0-1 range"""
        if column not in self.df.columns:
            return self.df
        
        min_val = self.df[column].min()
        max_val = self.df[column].max()
        
        if max_val == min_val:
            self.df[column] = 0
        else:
            self.df[column] = (self.df[column] - min_val) / (max_val - min_val)
        
        print(f"✓ Normalized column: {column}")
        return self.df
    
    def standardize_column(self, column):
        """Standardize column (z-score)"""
        if column not in self.df.columns:
            return self.df
        
        mean = self.df[column].mean()
        std = self.df[column].std()
        
        if std == 0:
            self.df[column] = 0
        else:
            self.df[column] = (self.df[column] - mean) / std
        
        print(f"✓ Standardized column: {column}")
        return self.df
    
    def create_bins(self, column, bins=5, labels=None):
        """Create binned categories from numeric column"""
        if column not in self.df.columns:
            return self.df
        
        if labels is None:
            labels = [f'Bin_{i+1}' for i in range(bins)]
        
        self.df[f'{column}_binned'] = pd.cut(self.df[column], bins=bins, labels=labels)
        
        print(f"✓ Created bins for {column}")
        return self.df
    
    def create_interaction(self, col1, col2, operation='multiply'):
        """Create interaction feature from two columns"""
        if col1 not in self.df.columns or col2 not in self.df.columns:
            return self.df
        
        if operation == 'multiply':
            self.df[f'{col1}_x_{col2}'] = self.df[col1] * self.df[col2]
        elif operation == 'add':
            self.df[f'{col1}_plus_{col2}'] = self.df[col1] + self.df[col2]
        elif operation == 'divide':
            self.df[f'{col1}_div_{col2}'] = self.df[col1] / self.df[col2].replace(0, 1)
        
        print(f"✓ Created interaction feature: {col1} {operation} {col2}")
        return self.df
    
    def encode_categorical(self, column, method='label'):
        """Encode categorical variables"""
        if column not in self.df.columns:
            return self.df
        
        if method == 'label':
            # Label encoding
            categories = self.df[column].unique()
            encoding = {cat: i for i, cat in enumerate(categories)}
            self.df[f'{column}_encoded'] = self.df[column].map(encoding)
            print(f"✓ Label encoded {column}")
        
        elif method == 'onehot':
            # One-hot encoding
            dummies = pd.get_dummies(self.df[column], prefix=column, drop_first=True)
            self.df = pd.concat([self.df, dummies], axis=1)
            print(f"✓ One-hot encoded {column}")
        
        return self.df
    
    def handle_temporal_features(self, date_column):
        """Extract temporal features from date column"""
        if date_column not in self.df.columns:
            return self.df
        
        try:
            self.df[date_column] = pd.to_datetime(self.df[date_column])
            
            self.df[f'{date_column}_year'] = self.df[date_column].dt.year
            self.df[f'{date_column}_month'] = self.df[date_column].dt.month
            self.df[f'{date_column}_day'] = self.df[date_column].dt.day
            self.df[f'{date_column}_dayofweek'] = self.df[date_column].dt.dayofweek
            self.df[f'{date_column}_quarter'] = self.df[date_column].dt.quarter
            
            print(f"✓ Extracted temporal features from {date_column}")
        except Exception as e:
            print(f"✗ Error processing {date_column}: {str(e)}")
        
        return self.df
    
    def get_processed_data(self):
        """Return processed dataframe"""
        return self.df
    
    def get_statistics(self):
        """Get statistics about transformations"""
        return {
            'original_rows': len(self.original_df),
            'processed_rows': len(self.df),
            'removed_rows': len(self.original_df) - len(self.df),
            'original_columns': len(self.original_df.columns),
            'processed_columns': len(self.df.columns),
            'new_columns': len(self.df.columns) - len(self.original_df.columns)
        }


def example_usage():
    """Example of advanced data processing"""
    print("\n" + "="*60)
    print("  ADVANCED DATA PROCESSING EXAMPLES")
    print("="*60 + "\n")
    
    # Create sample data
    sample_data = {
        'Sales': [100, 150, 200, 250, 300, 5000],  # Last value is outlier
        'Quantity': [5, 7, 10, 12, 15, 200],
        'Category': ['A', 'B', 'A', 'C', 'B', 'A'],
        'Date': ['2024-01-01', '2024-01-02', '2024-02-01', '2024-02-15', '2024-03-01', '2024-03-10']
    }
    
    df = pd.DataFrame(sample_data)
    processor = AdvancedDataProcessor(df)
    
    print("Original Data:")
    print(df)
    print(f"\nShape: {df.shape}\n")
    
    # Apply transformations
    print("Applying transformations...\n")
    
    # Remove outliers
    processor.handle_outliers_iqr('Sales', multiplier=1.5)
    
    # Normalize Sales
    processor.normalize_column('Sales')
    
    # Create bins
    processor.create_bins('Quantity', bins=3, labels=['Low', 'Medium', 'High'])
    
    # Create interaction
    processor.create_interaction('Sales', 'Quantity', 'multiply')
    
    # Encode categorical
    processor.encode_categorical('Category', method='onehot')
    
    # Extract temporal features
    processor.handle_temporal_features('Date')
    
    # Get results
    result_df = processor.get_processed_data()
    stats = processor.get_statistics()
    
    print("\nProcessed Data:")
    print(result_df)
    print(f"\nProcessing Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n" + "="*60 + "\n")


if __name__ == '__main__':
    example_usage()
