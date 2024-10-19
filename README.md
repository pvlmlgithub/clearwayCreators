# clearwayCreators
Traffic Management and Congestion Prediction System based on AI Power
Traffic Congestion Prediction: It uses random forest and FB prophet to predict traffic congestion with historical & real time data.
Alternative Route Suggestions: Scoring multiple possible routes using travel time, vehicle count, traffic signals, and recommends the best route.
Real-Time Data Integration: Pulls real time data from various sources through APIs: weather data, traffic sensors, cameras.
Route Evaluation and Optimization: It scores routes according to key factors such as average speed and travel time, and recommends most efficient routes.
Signal Timing Optimization: This forecasts vehicle counts over time in order to optimise traffic signal timings and remove bottlenecks.
Environmental Impact Reduction: It reduces fuel consumption and emissions by balancing traffic.

Technologies Used
Machine Learning:
Travel times were predicted based on traffic, weather and road conditions through a Random Forest Regressor.
FB Prophet (vehicle counts time series forecasting model)
API Integration:
Real time weather data from OpenWeatherMap API
Real time traffic data and route optimization using Google Maps API
Programming Languages: Python
Libraries/Frameworks:
Random Forest model build using scikit-learn
Time series forecasting – FB Prophet


