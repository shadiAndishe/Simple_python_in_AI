def choose_model(data_size, num_features, problem_type):
    if data_size > 100000:
        model = "Random Forest" if problem_type == "binary" else "Gradient Boosting"
    elif num_features < 10:
        model = "Logistic Regression"
    else:
        model = "SVM" if problem_type == "binary" else "Multinomial Naive Bayes"
    return model

data_size = 50000
num_features = 15
problem_type = "binary"
selected_model = choose_model(data_size, num_features, problem_type)
print(f"Selected model: {selected_model}")
