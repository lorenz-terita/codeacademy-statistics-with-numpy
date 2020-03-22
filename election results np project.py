import codecademylib
from matplotlib import pyplot as plt
import numpy as np

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']
total_ceballos= sum([1 for response in survey_responses if response == 'Ceballos'])
#print(total_ceballos)
survey_length = float(len(survey_responses))
percentage_ceballos= total_ceballos / survey_length
print(percentage_ceballos)
possible_surveys = np.random.binomial(survey_length, .54, size= 10000)/survey_length
plt.hist(possible_surveys, range=(0,1), bins=20)
plt.show()
possible_survey_length= float(len(possible_surveys))
incorrect_predictions= len(possible_surveys[possible_surveys < .5])
ceballos_loss_surveys= incorrect_predictions/possible_survey_length
print(ceballos_loss_surveys)
large_survey_length= float(7000)
large_surveys = np.random.binomial(large_survey_length, .54, size=10000)/large_survey_length
incorrect_predictions= len(large_surveys[large_surveys < .5])
ceballos_loss_new = incorrect_predictions/large_survey_length
print(ceballos_loss_new)
