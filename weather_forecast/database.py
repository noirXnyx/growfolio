#  sqlalchemy imports: create_engine is used to create a connection to the db, allowing interaction with the db
# Column, Integer, Float: these are used to define the schema in the db
# declarative_base - used to create a base class for declarative class definitions, defining the structure of the db
# using python classes
# sessionmaker - factory for creating new SQLAlchemy Session objects,
# which manage connections and transactions with the database.
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Base handles the internal SQLAlchemy mechanics needed to map Python classes to database tables.
Base = declarative_base()

# This part is for creating/recreating the db table 'weather_data'
class WeatherRecord(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    latitude  = Column(Float)
    longitude = Column(Float)
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)
    avg_temp_Fahrenheit = Column(Float)
    min_temp_Fahrenheit = Column(Float)
    max_temp_Fahrenheit = Column(Float)
    avg_wind_speed_mph = Column(Float)
    min_wind_speed_mph = Column(Float)
    max_wind_speed_mph = Column(Float)
    sum_precipitation_inches = Column(Float)
    min_precipitation_inches = Column(Float)
    max_precipitation_inches = Column(Float)

def recreate_table():
    engine = create_engine('sqlite:///weather.db') # This creates a connection to an SQLite database file
                                                    # named weather.db. The sqlite:/// prefix indicates that
                                                    # the database is an SQLite file.
    Base.metadata.drop_all(engine)  # Drop all tables, this is useful for dynamic dates/resetting the db schema
    Base.metadata.create_all(engine)  # Recreate all tables
    return engine

def insert_weather_data(engine, weather_data):
    Session = sessionmaker(bind=engine)
    session = Session()

    # creates a new instance of WeatherRecord with attributes populated from the weather_data object
    record = WeatherRecord(
        latitude=weather_data.latitude,
        longitude=weather_data.longitude,
        month=weather_data.date.month,
        day=weather_data.date.day,
        year=weather_data.date.year,
        avg_temp_Fahrenheit=weather_data.avg_temp,
        min_temp_Fahrenheit=weather_data.min_temp,
        max_temp_Fahrenheit=weather_data.max_temp,
        avg_wind_speed_mph=weather_data.avg_wind_speed,
        min_wind_speed_mph=weather_data.min_wind_speed,
        max_wind_speed_mph=weather_data.max_wind_speed,
        sum_precipitation_inches=weather_data.sum_precipitation,
        min_precipitation_inches=weather_data.min_precipitation,
        max_precipitation_inches=weather_data.max_precipitation
        )
    session.add(record) #adds the new record to the session, staging it for insertion into the database.
    session.commit() #commits the transaction, which inserts the record into the database
    session.close() #closes the session, releasing the connection back to the connection pool

#querying and displaying weather data from the db
def query_weather_data(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    #executes a query that retrieves all records from the WeatherRecord table and stores them in the results list
    results = session.query(WeatherRecord).all()

    #The function loops through each record in results and prints its attributes in a formatted string
    for result in results:
        print(f"ID: {result.id}, Latitude: {result.latitude}, Longitude: {result.longitude}, "
              f"Month: {result.month}, Day: {result.day}, Year: {result.year}, "
              f"Avg Temp: {result.avg_temp_Fahrenheit}, Min Temp: {result.min_temp_Fahrenheit}, Max Temp: {result.max_temp_Fahrenheit}, "
              f"Avg Wind Speed: {result.avg_wind_speed_mph}, Minimum Wind Speed: {result.min_wind_speed_mph}, Maximum Wind Speed: {result.max_wind_speed_mph}, Sum Precipitation: {result.sum_precipitation_inches}, "
              f"Min Precipitation: {result.min_precipitation_inches}, Max Precipitation: {result.max_precipitation_inches}")

    session.close()
