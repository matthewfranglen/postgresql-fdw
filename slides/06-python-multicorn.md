##  Python Multicorn

You can write your Foreign Data Wrapper in Python

Well documented

Easier

Quicker

---

##  Easy to Write

```python
from multicorn import ForeignDataWrapper

class ExampleFDW(ForeignDataWrapper):

    def __init__(self, options, columns):
        super(ExampleFDW, self).__init__(options, columns)

    def execute(self, quals, columns):
        for index in range(20):
            yield {column_name: index for column_name in columns}
```

This is a complete Multicorn Foreign Data Wrapper

---

##  Core Functionality

The Multicorn Wrapper is not complete

 * No ANALYZE support

 * No advance warning for modifications

 * No JOIN paths

 * Postgres always checks WHERE clauses<br>
<small>(just add a passing value to the results)</small>

---

##  Prototyping

Writing Foreign Data Wrappers with Python is fast

Most data stores have excellent Python Libraries

Performance critical wrappers should be rewritten in C
