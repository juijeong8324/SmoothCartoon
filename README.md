# SmoothCartoon

원하는 이미지를 Cartoon Style로 바꿔주는 프로그램입니다.

```python
def cartoonize(img):
  kernel_size = 7 # 5
  line_size = 7 # 7
  # Create Edge Mask
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to grayScale
  gray_blur = cv2.medianBlur(gray, kernel_size) # Smoothing
  edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, kernel_size)
  edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

  blurred = cv2.bilateralFilter(img, d=10, sigmaColor=250,sigmaSpace=250) # reduce noise
  cartoon = cv2.bitwise_and(blurred, edges)
  return cartoon
```

- `medianBlur()` : Gray image에 smoothing을 해주어 노이즈를 제거합니다. 보다 명확한 edge를 찾아줍니다.
  ![not median](/img/image-1.png)

  - medianBlur() 적용 안 했을 때 edge

  ![median](/img/image-2.png)

  - medianBlur() 적용 했을 때 edge

- `adaptiveThreshold()` : edge를 찾아줍니다.
- `bilateralFilter()` : edge를 유지하되 noise를 제거해주는 filter 입니다.
  ![Alt text](/img/image-3.png)
  - 원본 vs bilateralFilter

<br>

### 잘된 예

![test2](/img/image-5.png)
![test3](/img/image-6.png)

<br>

### 잘 안된 예

![test2](/img/image-10.png)
![test3](/img/image-9.png)

<br>

### 한계

![test](/img/image-7.png)
![Alt text](/img/image-8.png)

- 인물 사진의 경우 얼굴이 작을 때 이목구비를 세밀하게 나타내기 어렵고 원본과 비교했을 때 얼굴을 알아보기 힘들다

![test](/img/image-7.png)

- 대비가 비슷한 경우 edge를 찾기 힘들다. (머리 부분에 edge가 보이지 않는다.)

- 색의 대비가 명확한 경우와 명확하지 않은 경우, 좋은 cartoon style을 적용하기 위한 kernerl size와 line size가 다르다.
  EX) kernel = 3 line = 7
  ![good](/img/good.png)
  - 잘된 예
    ![bad](/img/bad.png)
  - 잘 안된 예
