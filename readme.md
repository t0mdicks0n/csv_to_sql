### CSV To SQL Command Line Tool

Use case:
- As a data scientist/analyst I often get small to medium size CSV:s with data from external sources which I want to import to my SQL database to query in conjunction with my other data.
  - This was one of those small things that I had to do on a weekly basis for a while and I got as frustrated each time since it's not intellectual challenging but fiddly.

#### How to run
```bash
python main.py test.csv ""
```
- The first argument is the file I want to format
- The second argument is to which directory I want to write down the output file.

(I am gonna change this to more intuitive flags for passing in arguments)


