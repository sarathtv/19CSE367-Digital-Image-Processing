rgbImage = imread('llama.jpg');
windowWidth = 7;
kernel = ones(windowWidth) / windowWidth .^ 2;
subplot(2, 1, 1);
imshow(rgbImage);
blurryImage = imfilter(rgbImage, kernel,'replicate');
subplot(2, 1, 2);
imshow(blurryImage);