A = imread('cameraman.tif');    
[histIM, bins] = imhist(A);
counts = histcounts(A);
cdf = cumsum(counts) / sum(counts);
figure
plot(cdf); 
