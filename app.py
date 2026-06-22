from flask import Flask, request, render_template_string
import time
import random

app = Flask(**name**)

def interpolation_search(arr, target):
low, high = 0, len(arr) - 1
comparisons = 0

```
while low <= high and arr[low] <= target <= arr[high]:
    comparisons += 1

    if low == high:
        if arr[low] == target:
            return low, comparisons
        return -1, comparisons

    if arr[high] == arr[low]:
        break

    pos = low + int(
        ((target - arr[low]) * (high - low))
        / (arr[high] - arr[low])
    )

    if arr[pos] == target:
        return pos, comparisons
    elif arr[pos] < target:
        low = pos + 1
    else:
        high = pos - 1

return -1, comparisons
```

def binary_search(arr, target):
low, high = 0, len(arr) - 1
comparisons = 0

```
while low <= high:
    comparisons += 1
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

return -1, comparisons
```

HTML = """

<!DOCTYPE html>

<html>
<head>
    <title>Interpolation Search Analysis</title>
    <style>
        body{
            font-family: Arial, sans-serif;
            margin:40px;
        }

```
    input{
        padding:8px;
        width:400px;
    }

    button{
        padding:10px 20px;
        margin-top:10px;
    }

    table{
        border-collapse: collapse;
        width:100%;
        margin-top:20px;
    }

    th, td{
        border:1px solid black;
        padding:8px;
        text-align:center;
    }

    th{
        background:#f2f2f2;
    }
</style>
```

</head>
<body>

<h1>Interpolation Search Performance Analysis</h1>

<form method="POST">
    <label>Enter Sorted Array Elements (space separated)</label><br><br>

```
<input type="text" name="array" required
       placeholder="2 5 10 15 23 35 48 60"><br><br>

<label>Enter Target Element</label><br><br>

<input type="number" name="target" required><br><br>

<button type="submit">Search</button>
```

</form>

{% if searched %}

<hr>

<h2>Search Result</h2>

<p><b>Array:</b> {{ arr }}</p>

<p><b>Searching for:</b> {{ target }}</p>

{% if idx != -1 %}

<p><b>Found at index:</b> {{ idx }}</p>
{% else %}
<p><b>Element not found</b></p>
{% endif %}

<p><b>Comparisons:</b> {{ comparisons }}</p>

<h2>Performance Analysis</h2>

<table>
<tr>
<th>Size</th>
<th>IS Time(ms)</th>
<th>BS Time(ms)</th>
<th>IS Comparisons</th>
<th>BS Comparisons</th>
</tr>

{% for row in performance_data %}

<tr>
<td>{{ row.size }}</td>
<td>{{ row.is_time }}</td>
<td>{{ row.bs_time }}</td>
<td>{{ row.comp_is }}</td>
<td>{{ row.comp_bs }}</td>
</tr>
{% endfor %}

</table>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

```
searched = False
arr = []
target = None
idx = None
comparisons = None
performance_data = []

if request.method == "POST":

    searched = True

    arr = list(map(int, request.form["array"].split()))
    arr.sort()

    target = int(request.form["target"])

    idx, comparisons = interpolation_search(arr, target)

    sizes = [1000, 5000, 10000, 50000, 100000]

    for size in sizes:

        test_arr = sorted(random.sample(range(size * 10), size))
        test_target = test_arr[random.randint(0, size - 1)]

        start = time.perf_counter()

        for _ in range(100):
            _, comp_is = interpolation_search(
                test_arr,
                test_target
            )

        is_time = (
            (time.perf_counter() - start)
            / 100
            * 1000
        )

        start = time.perf_counter()

        for _ in range(100):
            _, comp_bs = binary_search(
                test_arr,
                test_target
            )

        bs_time = (
            (time.perf_counter() - start)
            / 100
            * 1000
        )

        performance_data.append({
            "size": size,
            "is_time": round(is_time, 4),
            "bs_time": round(bs_time, 4),
            "comp_is": comp_is,
            "comp_bs": comp_bs
        })

return render_template_string(
    HTML,
    searched=searched,
    arr=arr,
    target=target,
    idx=idx,
    comparisons=comparisons,
    performance_data=performance_data
)
```

if **name** == "**main**":
app.run(host="0.0.0.0", port=5000)
