##############################################################################
# Spurpoint Messaging
#
# database.py
# 
# Database class to handle all of the db activities...
# including creating a new database.
# 
# Creator: Todd Smith
# Start Date: 2025-03-06
#
##############################################################################

import sqlite3
import os

class Database:
    """A general purpose class for managing SpurPoint SQLite databases
    
    This class uses a singleton object structure to ensure only one
    instance of the class is in use during the life of the application.
    """

    _instance = None

    def __new__(cls, db_name: str=os.path.join("SPMessaging.db"), opening: bool=False):
        """Instantiate a new instance of the database.
        
        If an instance does not already exist, create a new one.
        If the opening parameter is set to True, then the user has
        opened a different database and we need to start over with 
        a new instance.
        
        Parameters:
        db_name (str): path of the database to be opened
        opening (bool): True if opening a different database

        Returns:
        _instance (Database): a reference to this instance of the object
        """

        try:
                if cls._instance is None or opening: 
                        cls._instance = super(Database, cls).__new__(cls)
                        cls._instance.dbName = db_name

                        # if the db does not exist, create it; otherwise just open it.
                        if not os.path.exists(db_name):
                                cls._instance.conn = sqlite3.connect(db_name)
                                cls._instance.cursor = cls._instance.conn.cursor()
                                cls._instance.create_new_database()
                        else:
                                cls._instance.conn = sqlite3.connect(db_name)
                                cls._instance.cursor = cls._instance.conn.cursor()

                return cls._instance
            
        except:
            return None
    

    def execute_query(self, query: str, params: tuple=()) -> None:
        """Execute a non-returning SQL command
        
        This method is for commands such as UPDATE and INSERT that do
        not return any rows like a SELECT.
        
        Parameters:
        query (str): the query to be executed
        params (tuple): tuple or list of parameters (optional)
        """

        self.cursor.execute(query, params)
        self.conn.commit()


    def fetch_all(self, query: str, params: tuple=()) -> list:
        """Execute a SQL query
        
        This method is for retrieving rows from the database.
        
        Parameters:
        query (str): the sql query to be executed
        params (tuple): tuple or list of parameters (optional)
        """

        # construct a dictionary with column names as keys and execute
        self.cursor.execute(query, params)
        columns = [desc[0] for desc in self.cursor.description]  
        results = self.cursor.fetchall()

        # returns a list of dictionaries, one dict() for each row returned
        return [dict(zip(columns, row)) for row in results]  


    def fetch_many(self, row_limit: int, query: str, params: tuple=()) -> list:
        """Execute a SQL query, returning only the number of rows specified
        
        This method returns upto the number of rows specified in the
        row_limit. If row_limit=3 but only 2 rows match the query, only
        two rows are returned. However, if 5 rows match the query, only
        three rows are returned.
        
        Parameters:
        row_limit (int): the number of rows to return
        query (str): the sql query to be executed
        params (tuple): tuple or list of parameters (optional)
        """

        # construct a dictionary with column names as keys and execute
        self.cursor.execute(query, params)
        columns = [desc[0] for desc in self.cursor.description]  
        results = self.cursor.fetchmany(row_limit)

        # returns a list of dictionaries, one dict() for each row returned
        return [dict(zip(columns, row)) for row in results]  


    def execute_many(self, query: str, params: list=[]) -> None:
        """Executes SQL commands on a list a data
        
        This methods recieves a query string and a list of tuples for 
        parameters. The SQLite executemany method iterates through the
        list performing the SQL query on each tuple in the list.
        
        For example, given query='insert into runners (name, bib) values (?,?)'
        and params=[('Bob',5), ('John',10), ('Mary',12)], execute_many
        will insert three different records into the the runners table.
        
        Parameters:
        query (str): the query string to be executed
        params (list): a list of tuples representing multiple sets of params
        """

        self.cursor.executemany(query, params)
        self.conn.commit()

    
    def close(self):
        """Close the database connection"""

        self.conn.close()


    def create_new_database(self):
        """Creates the tables in a new database
        
        To make this class more generic, we may want to move this method
        outside the class.
        """

        # if the database file already exists, delete it.
        if os.path.exists(self.dbName): 
            # if a file exists, we have to close it before we delete to 
            # avoid a "File in use" error.
            self.conn.close()
            os.remove(self.dbName)

            self.conn = sqlite3.connect(self.dbName)
            self.cursor = self.conn.cursor()

        # create all the tables
        qry = '''CREATE TABLE Preferences (key TEXT PRIMARY KEY, value TEXT);'''
        self.execute_query(qry)

       
        qry = '''CREATE TABLE APRSMessages (
                MIdx INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                MsgID TEXT NOT NULL,
                MsgTime TEXT NOT NULL,
                MsgSource TEXT,
                MsgMessage TEXT,
                Acked INTEGER DEFAULT NULL,
                Purge INTEGER DEFAULT 0
                );'''
        self.execute_query(qry)


        
