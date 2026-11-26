# Data dictionary

Source: [Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments). Original notebook uses ten booking-time features. `target_no_show`: 1 missed, 0 attended. PatientId groups partitions; AppointmentID joins split assignments, not predictors. SMS_received is excluded because booking-time availability is unknown.

| Feature | Meaning |
|---|---|
| Age | Age in years |
| LeadTime_Days | Calendar days from booking to appointment |
| Scholarship | Source scholarship indicator |
| Hipertension | Source hypertension indicator |
| Diabetes | Source diabetes indicator |
| Alcoholism | Source alcoholism indicator |
| Handcap | Source disability-related field; preserve source encoding |
| Gender | Source recorded gender category |
| Neighbourhood | Source recorded neighborhood |
| Appointment_Weekday | Derived weekday |

The synthetic fixture generator produces patients, appointments, scheduling booking features, insurance verifications, frame and contact lens orders and, when inference is available, saved no-show scores. These are demonstration records, not real clinic observations. The prototype schema is defined by its generator and gateway code.
