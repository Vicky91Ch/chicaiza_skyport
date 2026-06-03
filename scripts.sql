CREATE USER chicaiza_skyport_user WITH PASSWORD 'admin123';
CREATE DATABASE chicaiza_skyport_db OWNER chicaiza_skyport_user;

\c chicaiza_skyport_db

ALTER SCHEMA public OWNER TO chicaiza_skyport_user;
GRANT ALL ON SCHEMA public TO chicaiza_skyport_user;
GRANT CREATE ON SCHEMA public TO chicaiza_skyport_user;

ALTER DEFAULT PRIVILEGES FOR USER chicaiza_skyport_user IN SCHEMA public
GRANT ALL ON TABLES TO chicaiza_skyport_user;

ALTER DEFAULT PRIVILEGES FOR USER chicaiza_skyport_user IN SCHEMA public
GRANT ALL ON SEQUENCES TO chicaiza_skyport_user;

ALTER DEFAULT PRIVILEGES FOR USER chicaiza_skyport_user IN SCHEMA public
GRANT ALL ON FUNCTIONS TO chicaiza_skyport_user;
