# erajp: Convert datetime to Japanese era

## Requirements
- Python 2.7+, 3.4+

## Installation
Comming soon!

## How to use

```
>>> strjpftime()
 'H27.08.05' # now
>>> strjpftime(datetime.datetime(1989, 1, 8)) 
 'H1.01.08'
>>> strjpftime(datetime.datetime(1989, 1, 8), u"%O%E年")
 '平成元年'
```

## License
MIT License