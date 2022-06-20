# Signlanguage Converter API Server Example

```sh
pip install -r requirements.txt
```

## Route
1. (Get) `/animation` - returns all examples
2. (Get) `/animation/example_1`

이 예제는 유니티 런타임에서만 사용되어야 할 데이터를 함께 반환하고 있습니다. 각 `Motion` 데이터의 `resPath`가 바로 그것입니다.

이후 `IDMotionConn` 데이터만 반환하도록 변경할 예정입니다.
