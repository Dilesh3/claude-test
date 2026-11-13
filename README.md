hello

## Factorial program

`factorial.py` asks for a non-negative integer and prints its factorial.

```bash
python3 factorial.py
```

![factorial.py running](images/factorial-run.png)

## Tests

`test_factorial.py` uses pytest to check:

| Test | What it checks |
|---|---|
| `test_known_values` | 0!, 1!, 2!, 3!, 5!, 10! give the expected results |
| `test_matches_math_factorial` | results for 0–29 match Python's `math.factorial` |
| `test_large_number` | 100! is computed correctly |
| `test_recurrence` | n! = n × (n−1)! for n = 1–49 |
| `test_negative_raises` | negative input raises `ValueError` |
| `test_cli_valid_input` | running the script with input `5` prints `5! = 120` |
| `test_cli_negative_input` | running the script with `-3` prints the error message |
| `test_cli_non_integer_input` | running the script with `abc` prints an error |

Run them with:

```bash
pip install pytest
python3 -m pytest -v
```

### Test report

**Result: 44 passed, 0 failed** (Python 3.13.18, pytest 9.2.0)

<details>
<summary>Full pytest output</summary>

```
============================= test session starts ==============================
platform linux -- Python 3.13.18, pytest-9.2.0, pluggy-1.7.0 -- /usr/local/bin/python3
cachedir: .pytest_cache
rootdir: /home/user/claude-test
plugins: anyio-4.15.1
collecting ... collected 44 items

test_factorial.py::test_known_values[0-1] PASSED                         [  2%]
test_factorial.py::test_known_values[1-1] PASSED                         [  4%]
test_factorial.py::test_known_values[2-2] PASSED                         [  6%]
test_factorial.py::test_known_values[3-6] PASSED                         [  9%]
test_factorial.py::test_known_values[5-120] PASSED                       [ 11%]
test_factorial.py::test_known_values[10-3628800] PASSED                  [ 13%]
test_factorial.py::test_matches_math_factorial[0] PASSED                 [ 15%]
test_factorial.py::test_matches_math_factorial[1] PASSED                 [ 18%]
test_factorial.py::test_matches_math_factorial[2] PASSED                 [ 20%]
test_factorial.py::test_matches_math_factorial[3] PASSED                 [ 22%]
test_factorial.py::test_matches_math_factorial[4] PASSED                 [ 25%]
test_factorial.py::test_matches_math_factorial[5] PASSED                 [ 27%]
test_factorial.py::test_matches_math_factorial[6] PASSED                 [ 29%]
test_factorial.py::test_matches_math_factorial[7] PASSED                 [ 31%]
test_factorial.py::test_matches_math_factorial[8] PASSED                 [ 34%]
test_factorial.py::test_matches_math_factorial[9] PASSED                 [ 36%]
test_factorial.py::test_matches_math_factorial[10] PASSED                [ 38%]
test_factorial.py::test_matches_math_factorial[11] PASSED                [ 40%]
test_factorial.py::test_matches_math_factorial[12] PASSED                [ 43%]
test_factorial.py::test_matches_math_factorial[13] PASSED                [ 45%]
test_factorial.py::test_matches_math_factorial[14] PASSED                [ 47%]
test_factorial.py::test_matches_math_factorial[15] PASSED                [ 50%]
test_factorial.py::test_matches_math_factorial[16] PASSED                [ 52%]
test_factorial.py::test_matches_math_factorial[17] PASSED                [ 54%]
test_factorial.py::test_matches_math_factorial[18] PASSED                [ 56%]
test_factorial.py::test_matches_math_factorial[19] PASSED                [ 59%]
test_factorial.py::test_matches_math_factorial[20] PASSED                [ 61%]
test_factorial.py::test_matches_math_factorial[21] PASSED                [ 63%]
test_factorial.py::test_matches_math_factorial[22] PASSED                [ 65%]
test_factorial.py::test_matches_math_factorial[23] PASSED                [ 68%]
test_factorial.py::test_matches_math_factorial[24] PASSED                [ 70%]
test_factorial.py::test_matches_math_factorial[25] PASSED                [ 72%]
test_factorial.py::test_matches_math_factorial[26] PASSED                [ 75%]
test_factorial.py::test_matches_math_factorial[27] PASSED                [ 77%]
test_factorial.py::test_matches_math_factorial[28] PASSED                [ 79%]
test_factorial.py::test_matches_math_factorial[29] PASSED                [ 81%]
test_factorial.py::test_large_number PASSED                              [ 84%]
test_factorial.py::test_recurrence PASSED                                [ 86%]
test_factorial.py::test_negative_raises[-1] PASSED                       [ 88%]
test_factorial.py::test_negative_raises[-5] PASSED                       [ 90%]
test_factorial.py::test_negative_raises[-100] PASSED                     [ 93%]
test_factorial.py::test_cli_valid_input PASSED                           [ 95%]
test_factorial.py::test_cli_negative_input PASSED                        [ 97%]
test_factorial.py::test_cli_non_integer_input PASSED                     [100%]

============================== 44 passed in 0.12s ==============================
```

</details>
