import unittest
from sqlalchemy.orm import sessionmaker
from database import recreate_table, query_weather_data, WeatherRecord
from weather_data import WeatherData
from datetime import datetime

class TestWeatherDataDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Print all data inserted in the tests
        print("All records inserted/used in the test database:")

        # Set up the database for testing
        cls.engine = recreate_table()

        # Example weather data to be inserted
        cls.weather_data = WeatherData(latitude=40.0806, longitude=-80.9001, date=datetime(2024, 8, 29))
        cls.weather_data.avg_temp = 52.6
        cls.weather_data.min_temp = -7.3
        cls.weather_data.max_temp = 94.8
        cls.weather_data.avg_wind_speed = 10.0
        cls.weather_data.min_wind_speed = 5.0
        cls.weather_data.max_wind_speed = 15.0
        cls.weather_data.sum_precipitation = 233.872
        cls.weather_data.min_precipitation = 0.0
        cls.weather_data.max_precipitation = 2.0

    def test_insert_weather_data(self):
        #Test inserting weather data into the db
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # Convert WeatherData to WeatherRecord
        record = WeatherRecord(
            latitude=self.weather_data.latitude,
            longitude=self.weather_data.longitude,
            month=self.weather_data.date.month,
            day=self.weather_data.date.day,
            year=self.weather_data.date.year,
            avg_temp_Fahrenheit=self.weather_data.avg_temp,
            min_temp_Fahrenheit=self.weather_data.min_temp,
            max_temp_Fahrenheit=self.weather_data.max_temp,
            avg_wind_speed_mph=self.weather_data.avg_wind_speed,
            min_wind_speed_mph=self.weather_data.min_wind_speed,
            max_wind_speed_mph=self.weather_data.max_wind_speed,
            sum_precipitation_inches=self.weather_data.sum_precipitation,
            min_precipitation_inches=self.weather_data.min_precipitation,
            max_precipitation_inches=self.weather_data.max_precipitation
        )

        session.add(record)
        session.commit()

        # Query the inserted data
        result = session.query(WeatherRecord).filter_by(latitude=40.0806, longitude=-80.9001).first()

        # Test if the data inserted correctly
        self.assertIsNotNone(result)
        self.assertEqual(result.latitude, 40.0806)
        self.assertEqual(result.longitude, -80.9001)
        self.assertEqual(result.avg_temp_Fahrenheit, 52.6)
        self.assertEqual(result.min_temp_Fahrenheit, -7.3)
        self.assertEqual(result.max_temp_Fahrenheit, 94.8)
        self.assertEqual(result.avg_wind_speed_mph, 10.0)
        self.assertEqual(result.min_wind_speed_mph, 5.0)
        self.assertEqual(result.max_wind_speed_mph, 15.0)
        self.assertEqual(result.sum_precipitation_inches, 233.872)
        self.assertEqual(result.min_precipitation_inches, 0.0)
        self.assertEqual(result.max_precipitation_inches, 2.0)

        session.close()

    def test_query_weather_data(self):
        #Test querying weather data from the database
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # Insert a record
        record = WeatherRecord(
            latitude=self.weather_data.latitude,
            longitude=self.weather_data.longitude,
            month=self.weather_data.date.month,
            day=self.weather_data.date.day,
            year=self.weather_data.date.year,
            avg_temp_Fahrenheit=self.weather_data.avg_temp,
            min_temp_Fahrenheit=self.weather_data.min_temp,
            max_temp_Fahrenheit=self.weather_data.max_temp,
            avg_wind_speed_mph=self.weather_data.avg_wind_speed,
            min_wind_speed_mph=self.weather_data.min_wind_speed,
            max_wind_speed_mph=self.weather_data.max_wind_speed,
            sum_precipitation_inches=self.weather_data.sum_precipitation,
            min_precipitation_inches=self.weather_data.min_precipitation,
            max_precipitation_inches=self.weather_data.max_precipitation
        )

        session.add(record)
        session.commit()
        session.close()

        # Test the query_weather_data function
        query_weather_data(self.engine)  # This should print the inserted data

    def test_insert_multiple_records(self):
        #Test inserting multiple records into the database.
        Session = sessionmaker(bind=self.engine)
        session = Session()

        # Insert the first record
        record1 = WeatherRecord(
            latitude=self.weather_data.latitude,
            longitude=self.weather_data.longitude,
            month=self.weather_data.date.month,
            day=self.weather_data.date.day,
            year=self.weather_data.date.year,
            avg_temp_Fahrenheit=self.weather_data.avg_temp,
            min_temp_Fahrenheit=self.weather_data.min_temp,
            max_temp_Fahrenheit=self.weather_data.max_temp,
            avg_wind_speed_mph=self.weather_data.avg_wind_speed,
            min_wind_speed_mph=self.weather_data.min_wind_speed,
            max_wind_speed_mph=self.weather_data.max_wind_speed,
            sum_precipitation_inches=self.weather_data.sum_precipitation,
            min_precipitation_inches=self.weather_data.min_precipitation,
            max_precipitation_inches=self.weather_data.max_precipitation
        )
        session.add(record1)

        # Insert a second record with different data
        weather_data_2 = WeatherData(latitude=35.6895, longitude=139.6917, date=datetime(2023, 7, 15))
        weather_data_2.avg_temp = 75.0
        weather_data_2.min_temp = 68.0
        weather_data_2.max_temp = 82.0
        weather_data_2.avg_wind_speed = 5.0
        weather_data_2.min_wind_speed = 3.0
        weather_data_2.max_wind_speed = 7.0
        weather_data_2.sum_precipitation = 10.5
        weather_data_2.min_precipitation = 0.2
        weather_data_2.max_precipitation = 1.5

        record2 = WeatherRecord(
            latitude=weather_data_2.latitude,
            longitude=weather_data_2.longitude,
            month=weather_data_2.date.month,
            day=weather_data_2.date.day,
            year=weather_data_2.date.year,
            avg_temp_Fahrenheit=weather_data_2.avg_temp,
            min_temp_Fahrenheit=weather_data_2.min_temp,
            max_temp_Fahrenheit=weather_data_2.max_temp,
            avg_wind_speed_mph=weather_data_2.avg_wind_speed,
            min_wind_speed_mph=weather_data_2.min_wind_speed,
            max_wind_speed_mph=weather_data_2.max_wind_speed,
            sum_precipitation_inches=weather_data_2.sum_precipitation,
            min_precipitation_inches=weather_data_2.min_precipitation,
            max_precipitation_inches=weather_data_2.max_precipitation
        )
        session.add(record2)

        session.commit()

        # Query all records and check that both are inserted
        results = session.query(WeatherRecord).all()

        # Test if two records are inserted
        self.assertEqual(len(results), 2)

        # Test specific values of the second record
        second_record = session.query(WeatherRecord).filter_by(latitude=35.6895, longitude=139.6917).first()
        self.assertIsNotNone(second_record)
        self.assertEqual(second_record.latitude, 35.6895)
        self.assertEqual(second_record.longitude, 139.6917)
        self.assertEqual(second_record.avg_temp_Fahrenheit, 75.0)
        self.assertEqual(second_record.min_temp_Fahrenheit, 68.0)
        self.assertEqual(second_record.max_temp_Fahrenheit, 82.0)
        self.assertEqual(second_record.avg_wind_speed_mph, 5.0)
        self.assertEqual(second_record.min_wind_speed_mph, 3.0)
        self.assertEqual(second_record.max_wind_speed_mph, 7.0)
        self.assertEqual(second_record.sum_precipitation_inches, 10.5)
        self.assertEqual(second_record.min_precipitation_inches, 0.2)
        self.assertEqual(second_record.max_precipitation_inches, 1.5)

        session.close()

    @classmethod
    def tearDownClass(cls):
        # Clean up the database by removing all records inserted during testing.
        Session = sessionmaker(bind=cls.engine)
        session = Session()
        session.query(WeatherRecord).delete()
        session.commit()
        session.close()

if __name__ == "__main__":
    unittest.main()
