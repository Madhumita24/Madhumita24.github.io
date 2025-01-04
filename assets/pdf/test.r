# Generate random data
set.seed(123)
x <- rnorm(100, mean = 10, sd = 2)
y <- 2 * x + rnorm(100, mean = 0, sd = 1)

# Create a scatter plot
plot(x, y, main = "Scatter Plot", xlab = "X", ylab = "Y")

# Fit a linear regression model
model <- lm(y ~ x)

# Add regression line to the plot
abline(model, col = "red")

# Print summary of the model
summary(model)