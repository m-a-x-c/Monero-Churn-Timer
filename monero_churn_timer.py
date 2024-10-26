from scipy.stats import lognorm

days_to_wait_before_next_churn = lognorm.rvs(2.135, loc=0, scale=1.77, size=1)[0]
print(days_to_wait_before_next_churn)