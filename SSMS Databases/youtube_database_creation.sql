/*
Youtube Database Creation SSMS

Use this database to store the youtube video analytics and track data.
*/

CREATE DATABASE YouTubeAnalytics; --Run Seperately

USE YouTubeAnalytics;

CREATE TABLE VideoMetrics (
    Id INT PRIMARY KEY IDENTITY(1,1),
    VideoId VARCHAR(255),
    Title VARCHAR(255),
    URL VARCHAR(255),
    ViewCount INT,
    PublishedAt DATETIME,
    DateAdded DATETIME DEFAULT GETDATE()
);