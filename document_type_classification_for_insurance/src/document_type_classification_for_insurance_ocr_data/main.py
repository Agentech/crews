#!/usr/bin/env python
import sys
from document_type_classification_for_insurance_ocr_data.crew import DocumentTypeClassificationForInsuranceOcrDataCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'ocr_text': """Chewy Bear was presented on 3/15/2021 for: Illness-Lethargy/Other
Subjective
See 'Plan and Other Notes' section for patient history documentation, if pertinent.
Visit Info: Chewy Bear's visit began at 8:20 AM on 3/15/2021 and ended on 3/15/2021
Doctors Assisting or Consulting with Care:
Medical Authorization Release Signed?
Future appointment(s) scheduled for:
None agreed to by client
Dr. Jamila Y Echols
Yes
Patient Information on 3/15/2021
Name: Chewy Bear
Species: Canine
Breed: Terrier, Yorkshire
Gender: Male (Neutered)
Description: brn
Date of Birth: 9/30/2015
Optimum Wellness Plan: Active Care Plus
Microchip #: 985112007160438 Home Again
Chewy Bear has visited this Banfield Hospital 1 time.
Chewy Bear's first visit on 3/15/2021 at this hospital
Weight: 22.60 Lbs/10.25 Kgs
Preventive Care Given Due Date Preventive Care Given Due Date
Heartworm Prevention 3/15/2021 9/13/2021 Lyme Test 9/16/2020 9/16/2021
Flea Prevention 3/15/2021 4/14/2021 Ehrlichia test 9/16/2020 9/16/2021
Tick Prevention 3/15/2021 4/14/2021 Anaplasma Test 9/16/2020 9/16/2021
Roundworms 3/15/2021 9/11/2021 Blood Cell Count 3/15/2021 3/15/2022
Hookworms 3/15/2021 9/11/2021 Serum Chemistries 3/15/2021 3/15/2022
Rabies 9/2/2020 9/2/2023 Differential Exam 3/15/2021 3/15/2022
DAPP 6/11/2018 6/10/2021 Fecal Exam 3/15/2021 9/11/2021
Leptospirosis 11/23/2020 11/23/2021 Urine Specific Gravity 6/11/2018 6/11/2019
Bordetella 11/23/2020 11/23/2021 Urine Strip Tests 6/11/2018 6/11/2019
Lyme 11/23/2020 11/23/2021 Urine Sediment Exam 6/11/2018 6/11/2019
Heartworm Test 9/16/2020 9/16/2021
Time Printed: 1:15 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 1 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, March 15, 2021 8:20 AM
Care Provided at
Laurel MD on
Abnormal Findings:
Overall Condition Body Condition Score - Above Ideal
Ocular Epiphora on Left Eyelid Epiphora on Right Eyelid
Otic Aberrant Hair - Right Ear Aberrant Hair - Left Ear
Oral/Nasal Tartar on Teeth - Found Swelling/Inflammation of Gums - Found
Normal or Not Selected Findings:
Overall Condition Nutritional Evaluation Complete
Overall Condition - Good
Dehydration Level - No Dehydration
Overall Evaluation Complete
Coat and Skin Coat/Skin Normal
Respiratory Respiratory Normal
Cardiovascular Cardiovascular Normal
Abdominal Abdominal Normal
Urogenital Urogenital Normal
Perineal Perineal Normal
Musculoskeletal Musculoskeletal Normal
Neurological Neurological Normal
Laboratory Results: (é = above normal; ê = below normal; ********** = could not be evaluated)
Temperature: 100º F - Within Normal Limits
Heart Rate: 116/min - Within Normal Limits
Respiration: 40/min - Within Normal Limits
Capillary Refill Time: Under 2 Seconds
Exam was certified by Dr. Jamila Y Echols, DVM on 3/15/2021
Physical Exam Findings on 3/15/2021
Objective
Time Printed: 1:15 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 2 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, March 15, 2021 8:20 AM
Care Provided at
Laurel MD on
Recorded on 3/15/2021 9:15:39 AM
Test Name Result Units Range
Fecal - Roundworm Eggs NEGATIVE
Fecal - Hookworm Eggs NEGATIVE
Fecal - Whipworm Eggs NEGATIVE
Fecal - Giardia NEGATIVE
Fecal - Coccidia Oocysts NEGATIVE
Fecal - Tapeworms NEGATIVE
Fecal - Abnormal Bacteria NEGATIVE
Fecal - Significant Blood NEGATIVE
Fecal - 'Other' Eggs NEGATIVE
Recorded on 3/15/2021 9:38:17 AM
Test Name Result Units Range
Albumin (ALB) 3.6 g/dL (2.300-4.000)
Alkaline Phosphatase (ALKP) ê <10.0 U/L (23.000-212.000)
ALT/SGPT (ALT) 77.0 U/L (10.000-125.000)
BUN (Blood Urea Nitrogen) 17.0 mg/dL (7.000-27.000)
Calcium (CA) 10.3 mg/dL (7.900-12.000)
Cholesterol (CHOL) 276.0 mg/dL (110.000-320.000)
Creatinine (CREA) 1.1 mg/dL (0.500-1.800)
Gamma Glutamyl Transferase (GGT) 1.0 U/L (0.000-11.000)
Globulin (GLOB) 3.5 g/dL (2.500-4.500)
Glucose (GLU) 103.0 mg/dL (74.000-143.000)
Phosphorus (PHOS) 5.3 mg/dL (2.500-6.800)
Bilirubin, Total (TBIL) 0.3 mg/dL (0.000-0.900)
Protein, Total (TP) 7.1 g/dL (5.200-8.200)
ALB/Glob 1.0
BUN/Crea 15.0
Recorded on 3/15/2021 9:38:27 AM
Test Name Result Units Range
WBC 8.83 10^9/l (6.000-17.000)
Lymphocyte 2.490 10^9/l (1.000-4.800)
Monocyte 0.49 10^9/l (0.200-1.500)
Neutrophil 5.82 10^9/l (3.000-12.000)
Time Printed: 1:15 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 3 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, March 15, 2021 8:20 AM
Care Provided at
Laurel MD on
Neutrophil 5.82 10^9/l (3.000-12.000)
Eosinophil 0.03 10^9/l (0.000-0.800)
Basophil 0.01 10^9/l (0.000-0.400)
Lymphocyte, % 28.2 % (9.000-47.000)
Monocyte, % 5.5 % (2.000-12.000)
Neutrophil, % 65.8 % (42.000-84.000)
Eosinophil, % ê 0.3 % (1.000-18.000)
Basophil, % 0.1 % (0.000-1.100)
RBC Count (RBC) 7.77 10^12/l (5.500-8.500)
Hemoglobin (HGB) 17.3 g/dl (12.000-18.000)
Hematocrit (HCT) 52.26 % (37.000-55.000)
MCV 67.0 fl (60.000-77.000)
MCH 22.2 pg (19.500-24.500)
MCHC 33.1 g/dl (31.000-39.000)
RDW 16.8 % (14.000-20.000)
Platelet Count (PLT) 250.0 10^9/l (165.000-500.000)
PCT 0.290 % (0.150-0.390)
MPV é 11.4 fl (3.900-11.100)
Recorded on 3/15/2021 11:50:38 AM
Test Name Result Units Range
Canine Pancreas-Specific Lipase NORMAL
Hospital Comments: cPL normal
Recorded on 3/15/2021 11:51:06 AM
Test Name Result Units Range
Ear Swab Yeast NEGATIVE
Ear Swab Bacteria NEGATIVE
Ear Swab Mites NEGATIVE
Assessment
Tentative Diagnosis Status Date Hospital Team Member
Anorexia Undergoing Therapy 3/15/2021 1364 Laurel
Epiphora Stable/Persistent/Chronic 3/15/2021 1364 Laurel
Gingivitis Stable/Persistent/Chronic 3/15/2021 1364 Laurel
Malaise Undergoing Therapy 3/15/2021 1364 Laurel
Time Printed: 1:15 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 4 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, March 15, 2021 8:20 AM
Care Provided at
Laurel MD on
Patella Luxation, Medial, Grade 1 Stable/Persistent/Chronic 3/15/2021 1364 Laurel
Periodontal Disease Stage 2 Undergoing Therapy 3/15/2021 1364 Laurel
Otitis Externa, Medical Undergoing Therapy 9/2/2020 1182 Largo
Dental Calculus Undergoing Therapy 12/14/2019 1182 Largo
Anal Sacs, Full (Otherwise Normal) Needs Protocol 3/9/2019 1182 Largo
Patellar Luxation, Medical Stable/Persistent/Chronic 3/9/2019 1182 Largo
Cystitis Undergoing Therapy 6/11/2018 1006
Calverton
Otitis Externa, Medical Undergoing Therapy 3/3/2018 1006
Calverton
Constipation, Conservative Needs Protocol 11/18/2017 1006
Calverton
Dental Calculus Undergoing Therapy 7/6/2017 1182 Largo
Granuloma, Acral Lick Stable/Persistent/Chronic 7/6/2017 1182 Largo
Epiphora Stable/Persistent/Chronic 6/14/2017 1182 Largo
Patellar Luxation, Medical Needs Protocol 6/14/2017 1182 Largo
Pruritus Undergoing Therapy 6/14/2017 1182 Largo
Dental Calculus Undergoing Therapy 6/8/2017 1006
Calverton
Healthy Pet Needs Protocol 5/31/2017 1182 Largo
Plan and Other Notes
Prescribed and Administered Therapy for this visit/hospitalization:
(Reported by most recent date first)
3/15/2021
Office Visit - Completed
Blood Sample Collect / Prep - Completed
Comprehensive Exam - Canine - Completed
Exam - Dental - Completed
Otoscopic Exam - Complete - Completed
Express Anal Glands - Completed
Internal Organ Function Screen - Completed
Pedicure - Completed
Simparica Blue (22.1-44lbs) Single Dose - Completed
ProHeart 6 (<25lbs) Injection - Completed
Ear Swab with Cytology & Stain - Completed
CPL (Canine Pancreas-Specific Lipase) SNAP Test -
Completed
Physical Exam: Wellness Plan - Completed
Complete Blood Cell Count (CBC/5 part machine
differential) - Completed
Day Care for Optimum Exam - Completed
Ophthalmic Exam - Complete - Completed
Rectal Exam - Brief - Completed
Fecal Sample Collect / Prep - Completed
Intestinal Parasite Fecal Exam - Completed
Pyrantel Pamoate 50mg/ml (per ml) - Completed
Medical Waste Disposal Fee - Completed
Ear Hair Removal - Completed
Apoquel 5.4mg Tablet - Completed
Famotidine 10mg Tablet - Completed
Time Printed: 1:15 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 5 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, March 15, 2021 8:20 AM
Care Provided at
Laurel MD on
Additional Medical Notes documented for this visit/hospitalization:
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
3/15/2021 11:50 AM
Plan Echols, J. Thomas, T. Smith, S. 1364 Laurel
The Lab Results for CPL (Canine Pancreas-Specific Lipase) SNAP Test were manually entered.
3/15/2021 11:35 AM
Plan Echols, J. Thomas, T. Smith, S. 1364 Laurel
ProHeart Administration
Administered at: 03/15/2021 9:39 AM
Lot Number: 427934
Amount Given: 0.51 ml
Site of Administration: Left Front Leg
3/15/2021 10:55 AM
Plan Echols, J. Thomas, T. Smith, S. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 3/15/2021 Prescription #: 1364-12473626
Rx: Famotidine 10mg Tablet Manufacturer:
Instructions: Give 0.5 tablets every 12 hours for 4 days
Start tonight.
Give by mouth only.
Providing Doctor: Jamila Echols Quantity: 4.00
Discard By: 9/13/2021 Number of Refills: 0 Refill Expiration Date: 9/15/2021
3/15/2021 10:55 AM
Plan Echols, J. Thomas, T. Smith, S. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 3/15/2021 Prescription #: 1364-12473694
Rx: Apoquel 5.4mg Tablet Manufacturer:
Instructions: Give 1 tablet every 12 hours for 14 days
Give with food.
Give by mouth only.
Monitor for signs of intestinal upset (decreased appetite, vomiting, diarrhea).
Providing Doctor: Jamila Echols Quantity: 28.00
Discard By: 9/13/2021 Number of Refills: 0 Refill Expiration Date: 9/15/2021
3/15/2021 10:54 AM
Plan Echols, J. Thomas, T. Smith, S. 1364 Laurel
Cerenia 10mg/ml Injectable (per ml) - Completed
Banfield Foundation Donation - Completed
Famotidine 10mg/ml Injectable (per ml) - Completed
Time Printed: 1:15 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 6 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, March 15, 2021 8:20 AM
Care Provided at
Laurel MD on
Prescription transferred to external pharmacy on: 3/15/2021
Indicated Pharmacy: Unknown/Other
Rx: Alprazolam, 1 mg/tablet
Dosage instructions: Give 0.5 tablets every 24 hours for 10 days
Total Count: 5
# of refills: 0
Refill expiration date: 9/15/2021
Prescribing Doctor: Jamila Echols
Transferring Doctor: Jamila Echols
3/15/2021 8:53 AM
Plan Echols, J. Smith, S. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 3/15/2021 Prescription #: 1364-12473485
Rx: Simparica Blue (22.1-44lbs) Single Dose Manufacturer: Zoetis
Instructions: Give 1 chewable tablet every 30 days for 1 month
Providing Doctor: Jamila Echols Quantity: 1.00
Discard By: 9/13/2021 Number of Refills: 0 Refill Expiration Date: 9/15/2021
3/15/2021 8:53 AM
Plan Echols, J. Smith, S. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 3/15/2021 Prescription #: 1364-12473509
Rx: Pyrantel Pamoate 50mg/ml (per ml) Manufacturer: Apexa
Instructions: Give 2.2 mls one time
Providing Doctor: Jamila Echols Quantity: 2.20
Discard By: 9/13/2021 Number of Refills: 0 Refill Expiration Date: 9/15/2021
3/15/2021 8:25 AM
Plan Echols, J. Smith, S. 1364 Laurel
Treatment plan for Chewy Bear for $229.61 authorized by Connie Diaz via Phone, on 3/15/2021 8:25
AM. Provider Team Member- Sam
Yes Pedicure/AGE
Yes FTP single dose HWP proheart 6
Went over cost of bloodwork $164.36
3/15/2021 8:20 AM
Assessment Echols, J. Thomas, T. Smith, S. 1364 Laurel
Time Printed: 1:15 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 7 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, March 15, 2021 8:20 AM
Care Provided at
Laurel MD on
Patella Luxation
Malaise
Anorexia
Epiphora
Malaise Undergoing Therapy
Anorexia Therapy Declined
Anorexia Undergoing Therapy
Gingivitis Stable/Persistent/Chronic
Periodontal Disease Stage 2 Undergoing Therapy
Epiphora Stable/Persistent/Chronic
Patella Luxation, Medial, Grade 1 Stable/Persistent/Chronic
3/15/2021 8:20 AM
Objective Echols, J. Thomas, T. Smith, S. 1364 Laurel
PE: eent: dental calculus/gingivitis, ear hair AU, abd pal:wnl, heart and lung sounds:wnl, ms:wnl,
skin:wnl
3/15/2021 8:20 AM
Plan(Notes) Echols, J. Thomas, T. Smith, S. 1364 Laurel
comp exam
fecal: neg
CBC/Chem: Low ALKP, otherwise wnl
Ear swab and cytology: debris AU
Ear hair removal
pyrantel (50 mg/ml) 2.2 ml PO sent home
diphenhydramine inj (50 mg/ml) client declined
Proheart Inj (0.0227 ml/lb) 0.51 ml SQ
1. Prognosis: Good with recommendations, treatment, and owner compliance
2. Client Education: flea/tick and HW prevention, vaccine schedule, vaccine reactions
3. Recheck: 3-5 days
4. Follow up therapy: recheck malaise
***********************************************************************
3/15/2021 8:20 AM
Subjective Echols, J. Thomas, T. Smith, S. 1364 Laurel
Presented for a comprehensive exam and concerns about P not eating. Hasn't been eating well ever
since client's mother got surgery recently (a couple of weeks ago). P is really close to client's mom and
will get depressed when she isn't around and will not eat. P has been eating over the weekend. P
vomited once last week after not eating and it was yellow bile. P might have an ear infection too.
Home Care Instructions documented for this visit/hospitalization:
Time Printed: 1:15 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 8 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, March 15, 2021 8:20 AM
Care Provided at
Laurel MD on
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
None
Therapy presented & declined by the client for this visit/ hospitalization:
Cytopoint 30mg/ml Injectable (per vial) - Client Declines
Therapy considered but not medically necessary for this visit/hospitalization:
Superchem / CBC - Not Medically Necessary
Complete Blood Cell Count (CBC/5 part machine
differential) - Not Medically Necessary
Blood Sample Collect / Prep - Not Medically Necessary
Cytopoint Injection Administration - Not Medically
Necessary
Internal Organ Function Screen - Not Medically Necessary
Electrolytes (K, Na, Cl, Na/K) - Not Medically Necessary
Alprazolam 1mg Tablet - Not Medically Necessary
Therapy postponed by the client or doctor this visit/hospitalization:
None
Time Printed: 1:15 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 9 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, March 15, 2021 8:20 AM
Care Provided at
Laurel MD on
Chewy Bear was presented on 3/20/2021 for: Follow Up-Illness Recheck, recheck malaise
Subjective
See 'Plan and Other Notes' section for patient history documentation, if pertinent.
Visit Info: Chewy Bear's visit began at 10:36 AM on 3/20/2021 and ended on 3/20/2021
Doctors Assisting or Consulting with Care:
Medical Authorization Release Signed?
Future appointment(s) scheduled for:
None agreed to by client
Dr. Jamila Y Echols
Yes
Patient Information on 3/20/2021
Name: Chewy Bear
Species: Canine
Breed: Terrier, Yorkshire
Gender: Male (Neutered)
Description: brn
Date of Birth: 9/30/2015
Optimum Wellness Plan: Active Care Plus
Microchip #: 985112007160438 Home Again
Chewy Bear has visited this Banfield Hospital 2 times.
Chewy Bear's first visit on 3/15/2021 at this hospital
Chewy Bear's last visit on 3/20/2021 at this hospital
Weight: 20.80 Lbs/9.43 Kgs
Preventive Care Given Due Date Preventive Care Given Due Date
Heartworm Prevention 3/15/2021 9/13/2021 Lyme Test 9/16/2020 9/16/2021
Flea Prevention 3/15/2021 4/14/2021 Ehrlichia test 9/16/2020 9/16/2021
Tick Prevention 3/15/2021 4/14/2021 Anaplasma Test 9/16/2020 9/16/2021
Roundworms 3/15/2021 9/11/2021 Blood Cell Count 3/15/2021 3/15/2022
Hookworms 3/15/2021 9/11/2021 Serum Chemistries 3/15/2021 3/15/2022
Rabies 9/2/2020 9/2/2023 Differential Exam 3/15/2021 3/15/2022
DAPP 6/11/2018 6/10/2021 Fecal Exam 3/15/2021 9/11/2021
Leptospirosis 11/23/2020 11/23/2021 Urine Specific Gravity 6/11/2018 6/11/2019
Bordetella 11/23/2020 11/23/2021 Urine Strip Tests 6/11/2018 6/11/2019
Lyme 11/23/2020 11/23/2021 Urine Sediment Exam 6/11/2018 6/11/2019
Heartworm Test 9/16/2020 9/16/2021
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 1 of 5
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Saturday, March 20, 2021 10:36 AM
Care Provided at
Laurel MD on
Abnormal Findings:
Overall Condition Body Condition Score - Above Ideal
Ocular Epiphora on Left Eyelid Epiphora on Right Eyelid
Otic Aberrant Hair - Left Ear Aberrant Hair - Right Ear
Oral/Nasal Tartar on Teeth - Found Swelling/Inflammation of Gums - Found
Normal or Not Selected Findings:
Overall Condition Nutritional Evaluation Complete Overall Evaluation Complete
Coat and Skin Coat/Skin Normal
Respiratory Respiratory Normal
Cardiovascular Cardiovascular Normal
Abdominal Abdominal Normal
Urogenital Urogenital Normal
Perineal Perineal Normal
Musculoskeletal Musculoskeletal Normal
Neurological Neurological Normal
Temperature: 100º F -
Heart Rate: 120/min -
Respiration: 40/min -
Capillary Refill Time: Under 2 Seconds
Exam was certified by Dr. Jamila Y Echols, DVM on 3/20/2021
Physical Exam Findings on 3/20/2021
Objective
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 2 of 5
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Saturday, March 20, 2021 10:36 AM
Care Provided at
Laurel MD on
Additional Medical Notes documented for this visit/hospitalization:
(Reported by most recent date first)
Assessment
Tentative Diagnosis Status Date Hospital Team Member
Anorexia Condition Resolved 3/20/2021 1364 Laurel
Epiphora Stable/Persistent/Chronic 3/20/2021 1364 Laurel
Gingivitis Stable/Persistent/Chronic 3/20/2021 1364 Laurel
Malaise Condition Resolved 3/20/2021 1364 Laurel
Patella Luxation, Medial, Grade 1 Stable/Persistent/Chronic 3/20/2021 1364 Laurel
Periodontal Disease Stage 2 Undergoing Therapy 3/20/2021 1364 Laurel
Otitis Externa, Medical Undergoing Therapy 9/2/2020 1182 Largo
Dental Calculus Undergoing Therapy 12/14/2019 1182 Largo
Anal Sacs, Full (Otherwise Normal) Needs Protocol 3/9/2019 1182 Largo
Patellar Luxation, Medical Stable/Persistent/Chronic 3/9/2019 1182 Largo
Cystitis Undergoing Therapy 6/11/2018 1006
Calverton
Otitis Externa, Medical Undergoing Therapy 3/3/2018 1006
Calverton
Constipation, Conservative Needs Protocol 11/18/2017 1006
Calverton
Dental Calculus Undergoing Therapy 7/6/2017 1182 Largo
Granuloma, Acral Lick Stable/Persistent/Chronic 7/6/2017 1182 Largo
Epiphora Stable/Persistent/Chronic 6/14/2017 1182 Largo
Patellar Luxation, Medical Needs Protocol 6/14/2017 1182 Largo
Pruritus Undergoing Therapy 6/14/2017 1182 Largo
Dental Calculus Undergoing Therapy 6/8/2017 1006
Calverton
Healthy Pet Needs Protocol 5/31/2017 1182 Largo
Plan and Other Notes
Prescribed and Administered Therapy for this visit/hospitalization:
(Reported by most recent date first)
3/20/2021
Physical Exam: Follow Up (OWP) - Completed Office Visit: Follow Up - Completed
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 3 of 5
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Saturday, March 20, 2021 10:36 AM
Care Provided at
Laurel MD on
Date Type Note Doctor VT/VA CSC Hospital
6/12/2021 11:45 AM
Miscellaneous Entzminger, E. 1364 Laurel
Client inquired re status
Client was scheduled per instruction of our work group chat; client was given information for other
banfield clinics (MCP & Greenbelt) along with the dog and cat ER number
3/20/2021 10:37 AM
Assessment Echols, J. 1364 Laurel
Malaise Condition Resolved
Patella Luxation, Medial, Grade 1 Stable/Persistent/Chronic
Periodontal Disease Stage 2 Undergoing Therapy
Epiphora Stable/Persistent/Chronic
Anorexia Condition Resolved
Gingivitis Stable/Persistent/Chronic
3/20/2021 10:37 AM
Objective Echols, J. Rey, A. 1364 Laurel
PE: eent: dental calculus/gingivitis, ear hair AU, abd pal:wnl, heart and lung sounds:wnl, ms:wnl,
skin:wnl
3/20/2021 10:37 AM
Plan(Notes) Echols, J. 1364 Laurel
Physical exam
1. Prognosis: Good with recommendations, treatment, and owner compliance
2. Client Education: flea/tick and HW prevention, vaccine schedule, vaccine reactions
3. Recheck: 3 months
4. Follow up therapy: Vaccines
**********************************************
3/20/2021 10:37 AM
Subjective Echols, J. Rey, A. 1364 Laurel
P presented for an illness recheck. Client states that P is eating more and his licking is doing better since
the cytopoint inj.
Home Care Instructions documented for this visit/hospitalization:
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
None
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 4 of 5
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Saturday, March 20, 2021 10:36 AM
Care Provided at
Laurel MD on
Therapy presented & declined by the client for this visit/ hospitalization:
None
Therapy considered but not medically necessary for this visit/hospitalization:
None
Therapy postponed by the client or doctor this visit/hospitalization:
None
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 5 of 5
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Saturday, March 20, 2021 10:36 AM
Care Provided at
Laurel MD on
Chewy Bear was presented on 6/21/2021 for: Illness-Vomiting/Diarrhea/GI, vomiting
randomly
Subjective
See 'Plan and Other Notes' section for patient history documentation, if pertinent.
Visit Info: Chewy Bear's visit began at 8:55 AM on 6/21/2021 and ended on 6/21/2021
Doctors Assisting or Consulting with Care:
Medical Authorization Release Signed?
Future appointment(s) scheduled for:
None agreed to by client
Dr. Jamila Y Echols
Yes
Patient Information on 6/21/2021
Name: Chewy Bear
Species: Canine
Breed: Terrier, Yorkshire
Gender: Male (Neutered)
Description: brn
Date of Birth: 9/30/2015
Optimum Wellness Plan: Active Care Plus
Microchip #: 985112007160438 Home Again
Chewy Bear has visited this Banfield Hospital 3 times.
Chewy Bear's first visit on 3/15/2021 at this hospital
Chewy Bear's last visit on 6/21/2021 at this hospital
Weight: 26.40 Lbs/11.97 Kgs
Preventive Care Given Due Date Preventive Care Given Due Date
Heartworm Prevention 3/15/2021 9/13/2021 Lyme Test 9/16/2020 9/16/2021
Flea Prevention 6/21/2021 7/21/2021 Ehrlichia test 9/16/2020 9/16/2021
Tick Prevention 6/21/2021 7/21/2021 Anaplasma Test 9/16/2020 9/16/2021
Roundworms 3/15/2021 9/11/2021 Blood Cell Count 6/21/2021 12/18/2021
Hookworms 3/15/2021 9/11/2021 Serum Chemistries 6/21/2021 12/18/2021
Rabies 9/2/2020 9/2/2023 Differential Exam 6/21/2021 12/18/2021
DAPP 6/21/2021 6/21/2024 Electrolytes 6/21/2021 6/21/2022
Leptospirosis 11/23/2020 11/23/2021 Fecal Exam 3/15/2021 9/11/2021
Bordetella 11/23/2020 11/23/2021 Urine Specific Gravity 6/11/2018 6/11/2019
Lyme 11/23/2020 11/23/2021 Urine Strip Tests 6/11/2018 6/11/2019
Diphenhydramine 6/21/2021 6/22/2021 Urine Sediment Exam 6/11/2018 6/11/2019
Heartworm Test 9/16/2020 9/16/2021
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 1 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, June 21, 2021 8:55 AM
Care Provided at
Laurel MD on
Abnormal Findings:
Overall Condition Body Condition Score - Above Ideal
Ocular Epiphora on Left Eyelid Epiphora on Right Eyelid
Otic Aberrant Hair - Left Ear Aberrant Hair - Right Ear
Oral/Nasal Tartar on Teeth - Found Swelling/Inflammation of Gums - Found
Normal or Not Selected Findings:
Overall Condition Nutritional Evaluation Complete Overall Evaluation Complete
Coat and Skin Coat/Skin Normal
Respiratory Respiratory Normal
Cardiovascular Cardiovascular Normal
Abdominal Abdominal Normal
Urogenital Urogenital Normal
Perineal Perineal Normal
Musculoskeletal Musculoskeletal Normal
Neurological Neurological Normal
Laboratory Results: (é = above normal; ê = below normal; ********** = could not be evaluated)
Laboratory results have not yet been recorded for the following test(s): Radiology Abdomen
Temperature: 101.3º F -
Heart Rate: 130/min -
Respiration: Unable To Evaluate
Capillary Refill Time: Under 2 Seconds
Exam was certified by Dr. Jamila Y Echols, DVM on 6/21/2021
Physical Exam Findings on 6/21/2021
Objective
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 2 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, June 21, 2021 8:55 AM
Care Provided at
Laurel MD on
Recorded on 6/21/2021 4:41:08 PM
Test Name Result Units Range
Sodium (Na+) 156.0 mmol/L (144.000-160.000)
Potassium (K+) 3.9 mmol/L (3.500-5.800)
Chloride (CL-) 114.0 mmol/L (109.000-122.000)
Na+/K+ 40.0
Osmolality 307.0 mmol/kg
Recorded on 6/21/2021 4:42:25 PM
Test Name Result Units Range
Albumin (ALB) 3.5 g/dL (2.300-4.000)
Alkaline Phosphatase (ALKP) ê 11.0 U/L (23.000-212.000)
ALT/SGPT (ALT) 67.0 U/L (10.000-125.000)
BUN (Blood Urea Nitrogen) 13.0 mg/dL (7.000-27.000)
Calcium (CA) 10.0 mg/dL (7.900-12.000)
Cholesterol (CHOL) 282.0 mg/dL (110.000-320.000)
Creatinine (CREA) 0.9 mg/dL (0.500-1.800)
Gamma Glutamyl Transferase (GGT) 0.0 U/L (0.000-11.000)
Globulin (GLOB) 3.7 g/dL (2.500-4.500)
Glucose (GLU) 98.0 mg/dL (74.000-143.000)
Phosphorus (PHOS) 4.5 mg/dL (2.500-6.800)
Bilirubin, Total (TBIL) 0.5 mg/dL (0.000-0.900)
Protein, Total (TP) 7.2 g/dL (5.200-8.200)
ALB/Glob 0.9
BUN/Crea 14.0
Recorded on 6/21/2021 5:01:45 PM
Test Name Result Units Range
WBC 15.0 10^9/l (6.000-17.000)
Lymphocyte 3.14 10^9/l (1.000-4.800)
Monocyte 0.44 10^9/l (0.200-1.500)
Neutrophil 11.33 10^9/l (3.000-12.000)
Eosinophil 0.08 10^9/l (0.000-0.800)
Basophil 0.01 10^9/l (0.000-0.400)
Lymphocyte, % 20.9 % (9.000-47.000)
Monocyte, % 3.0 % (2.000-12.000)
Neutrophil, % 75.5 % (42.000-84.000)
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 3 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, June 21, 2021 8:55 AM
Care Provided at
Laurel MD on
Neutrophil, % 75.5 % (42.000-84.000)
Eosinophil, % ê 0.5 % (1.000-18.000)
Basophil, % 0.1 % (0.000-1.100)
RBC Count (RBC) 7.49 10^12/l (5.500-8.500)
Hemoglobin (HGB) 16.9 g/dl (12.000-18.000)
Hematocrit (HCT) 48.71 % (37.000-55.000)
MCV 65.0 fl (60.000-77.000)
MCH 22.6 pg (19.500-24.500)
MCHC 34.7 g/dl (31.000-39.000)
RDW 16.4 % (14.000-20.000)
Platelet Count (PLT) ê 135.0 10^9/l (165.000-500.000)
PCT ê 0.140 % (0.150-0.390)
MPV 10.7 fl (3.900-11.100)
Recorded on 6/21/2021 6:19:14 PM
Test Name Result Units Range
Canine Pancreas-Specific Lipase NORMAL
Hospital Comments: normal
Recorded on 8/22/2021 1:53:31 PM
Test Name Result Units Range
Interpretation of Radiographs NORMAL
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 4 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, June 21, 2021 8:55 AM
Care Provided at
Laurel MD on
Hospital Comments: ABDOMINAL RADIOGRAPHS: 21 June 2021: Three views are available for
interpretation.
FINDINGS: The liver and spleen are within normal limits for size, contour and
opacity. The urinary tract is within normal limits. The GI tract is within normal
limits without foreign material, over-distension or intestinal plication noted.
The serosal detail of the abdomen is normal. No skeletal abnormalities are
noted.
CONCLUSIONS: Unremarkable study. The source of GI signs is not identified.
Inflammatory bowel disease, infectious gastroenteritis, pancreatitis, dietary
intolerance, a systemic illness causing secondary GI signs and ingestion of nonobstructing
soft tissue opaque foreign material can be present causing signs
without findings radiographically. No signs of obstruction are noted although
this cannot be completely ruled out on survey radiographs.
RECOMMENDATIONS: Abdominal ultrasound is recommended if the clinical
signs do not respond to medical management of IBD and gastroenteritis.
Angela Hartman DVM, DACVR
If there are discrepancies between this report and your impressions, please
email nzevet@gmail.com to discuss the case. Thank you.
Assessment
Tentative Diagnosis Status Date Hospital Team Member
Epiphora Stable/Persistent/Chronic 6/21/2021 1364 Laurel
Gingivitis Stable/Persistent/Chronic 6/21/2021 1364 Laurel
Periodontal Disease Stage 2 Undergoing Therapy 6/21/2021 1364 Laurel
Vomiting, Conservative Undergoing Therapy 6/21/2021 1364 Laurel
Patella Luxation, Medial, Grade 1 Stable/Persistent/Chronic 3/20/2021 1364 Laurel
Otitis Externa, Medical Undergoing Therapy 9/2/2020 1182 Largo
Dental Calculus Undergoing Therapy 12/14/2019 1182 Largo
Anal Sacs, Full (Otherwise Normal) Needs Protocol 3/9/2019 1182 Largo
Patellar Luxation, Medical Stable/Persistent/Chronic 3/9/2019 1182 Largo
Cystitis Undergoing Therapy 6/11/2018 1006
Calverton
Otitis Externa, Medical Undergoing Therapy 3/3/2018 1006
Calverton
Constipation, Conservative Needs Protocol 11/18/2017 1006
Calverton
Dental Calculus Undergoing Therapy 7/6/2017 1182 Largo
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 5 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, June 21, 2021 8:55 AM
Care Provided at
Laurel MD on
Additional Medical Notes documented for this visit/hospitalization:
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
12/22/2021 12:06 AM
Historical 1364 Laurel
The Radiology Abdomen Lab was removed by a system process. Though these laboratory results were
done, they were not saved to this pet’s medical record in this area of the record. The placeholder for
these results was removed by an automatic system update. Results may be available within free-form
medical note text.
7/12/2021 4:06 PM
Granuloma, Acral Lick Stable/Persistent/Chronic 7/6/2017 1182 Largo
Epiphora Stable/Persistent/Chronic 6/14/2017 1182 Largo
Patellar Luxation, Medical Needs Protocol 6/14/2017 1182 Largo
Pruritus Undergoing Therapy 6/14/2017 1182 Largo
Dental Calculus Undergoing Therapy 6/8/2017 1006
Calverton
Healthy Pet Needs Protocol 5/31/2017 1182 Largo
Plan and Other Notes
Prescribed and Administered Therapy for this visit/hospitalization:
(Reported by most recent date first)
6/21/2021
Office Visit - Completed
CPL (Canine Pancreas-Specific Lipase) SNAP Test -
Completed
Radiology Abdomen - Completed
Superchem / CBC - Completed
Complete Blood Cell Count (CBC/5 part machine
differential) - Completed
Internal Organ Function Screen - Completed
Pre-Vaccination Package, High Risk Breed - Completed
Vaccine - Distemper Parvo DAPP - Completed
MRX RC Canine Gastrointestinal Fiber Response -
Completed
Express Anal Glands - Completed
Physical Exam: Wellness Plan - Completed
Radiograph Consult (Routine)-Digital Image -
Completed
Simparica Blue (22.1-44lbs) Single Dose - Completed
Blood Sample Collect / Prep - Completed
Electrolytes (K, Na, Cl, Na/K) - Completed
Medical Waste Disposal Fee - Completed
Diphenhydramine Injection (Pre-Vaccination) -
Completed
Famotidine 10mg Tablet - Completed
Proviable Forte Sprinkle Capsule (per capsule) -
Completed
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 6 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, June 21, 2021 8:55 AM
Care Provided at
Laurel MD on
Plan Echols, J. 1364 Laurel
Client notified re status
Called and spoke with owner about radiology report, which was wnl. Owner is now concerned with
patient joints. Informed owner that we took pics of the abdomen and not the joints. So we may need to
take a new set of radiographs. Informed owner to start patient on joint supplements and fish oil. Dr.
Echols
6/21/2021 6:19 PM
Plan Echols, J. Rey, A. Johnson-Downes, K. 1364 Laurel
The Lab Results for CPL (Canine Pancreas-Specific Lipase) SNAP Test were manually entered.
6/21/2021 5:59 PM
Plan Echols, J. Rey, A. Johnson-Downes, K. 1364 Laurel
Administered at: 06/21/2021 2:34 PM
Preventive Care: Vaccine - Distemper Parvo DAPP Route: Subcutaneous Site: Right Front Leg
Producer: Elanco Expiration Date: 6/21/2024
Lot Number: D364705A Lot Expiration:7/27/2022
Combination/Product Given: DAPP Alone (Duramune Max 5)
6/21/2021 5:01 PM
Plan Echols, J. Rey, A. Johnson-Downes, K. 1364 Laurel
The Lab Results for Complete Blood Cell Count (CBC/5 part machine differential) were manually
entered.
6/21/2021 3:46 PM
Plan Echols, J. Rey, A. Johnson-Downes, K. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 6/21/2021 Prescription #: 1364-12551058
Rx: Proviable Forte Sprinkle Capsule (per capsule) Manufacturer:
Instructions: Give 1 capsule every 24 hours for 14 days
Add to the food
Providing Doctor: Jamila Echols Quantity: 14.00
Discard By: 12/20/2021 Number of Refills: 0 Refill Expiration Date: 12/21/2021
6/21/2021 3:46 PM
Plan Echols, J. Rey, A. Johnson-Downes, K. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 6/21/2021 Prescription #: 1364-12551057
Rx: MRX RC Canine Gastrointestinal Fiber Response Manufacturer:
Instructions:
Providing Doctor: Jamila Echols Quantity: 1.00
Discard By: N/A Number of Refills: N/A Refill Expiration Date: N/A
6/21/2021 3:46 PM
Plan Echols, J. Rey, A. Johnson-Downes, K. 1364 Laurel
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 7 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, June 21, 2021 8:55 AM
Care Provided at
Laurel MD on
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 6/21/2021 Prescription #: 1364-12551059
Rx: Famotidine 10mg Tablet Manufacturer:
Instructions: Give 0.5 tablets every 12 hours for 7 days
Give by mouth only.
Providing Doctor: Jamila Echols Quantity: 7.00
Discard By: 12/20/2021 Number of Refills: 0 Refill Expiration Date: 12/21/2021
6/21/2021 2:34 PM
Plan Echols, J. Rey, A. Johnson-Downes, K. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 6/21/2021 Prescription #: 1364-12550801
Rx: Diphenhydramine Injection (Pre-Vaccination) Manufacturer:
Instructions: Inject 0.53 mls one time
Providing Doctor: Jamila Echols Quantity: 0.53
Discard By: 12/20/2021 Number of Refills: 0 Refill Expiration Date: 12/21/2021
6/21/2021 12:50 PM
Plan Echols, J. Rey, A. Johnson-Downes, K. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 6/21/2021 Prescription #: 1364-12550776
Rx: Simparica Blue (22.1-44lbs) Single Dose Manufacturer: Zoetis
Instructions: Give 1 chewable tablet every 30 days until gone
Providing Doctor: Jamila Echols Quantity: 1.00
Discard By: 12/20/2021 Number of Refills: 0 Refill Expiration Date: 12/21/2021
6/21/2021 8:55 AM
Assessment Echols, J. Rey, A. Johnson-Downes, K. 1364 Laurel
PD2
Vomiting r/o pancreatitis, parasites, FB, toxin ingestion
Epiphora Stable/Persistent/Chronic
Gingivitis Stable/Persistent/Chronic
Periodontal Disease Stage 2 Undergoing Therapy
Vomiting, Conservative Undergoing Therapy
6/21/2021 8:55 AM
Objective Echols, J. Johnson-Downes, K. 1364 Laurel
PE: eent: dental calculus/gingivitis, ear hair AU, abd pal:wnl, heart and lung sounds:wnl, ms:wnl,
skin:wnl
6/21/2021 8:55 AM
Plan(Notes) Echols, J. Rey, A. Johnson-Downes, K. 1364 Laurel
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 8 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, June 21, 2021 8:55 AM
Care Provided at
Laurel MD on
Physical Exam
CBC/Chem: see labs
cPL: normal
Rads: pending
Rads sent for routine consult: pending
AG expression
diphenhydramine inj (50 mg/ml) 0.52 ml IM prior to vax
DAPP 3 yrs
Declined:
Dispensed:
CE:
1. Prognosis: Good with current recommendations, treatment, and owner compliance
2. Client Education: flea/tick and HW prevention, vaccine schedule, vaccine reactions
3. Recheck: 2 weeks
4. Follow up therapy: Recheck vomiting
***********************************************************************
6/21/2021 8:55 AM
Subjective Echols, J. Rey, A. Johnson-Downes, K. 1364 Laurel
P presented for vomiting concerns. Client states that P has been vomiting for past 2-3 months "not
super often but he vomits a lot when he does". The vomiting happens every 2-3 weeks and is usually
yellow or the color of his food. sometimes has the food in it. Client's also recently adopted a bunny and
P seems to be hyper focused on it to the point where he won't eat. O wonders if P is overweight and if so
what to do. P has also been panting a lot more, likely due to the rabbit. P is not having diarrhea and is
drinking normally. P currently eats a mixture of hills dry food and hills healthy diet wet.
Home Care Instructions documented for this visit/hospitalization:
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
None
Therapy presented & declined by the client for this visit/ hospitalization:
None
Therapy considered but not medically necessary for this visit/hospitalization:
None
Therapy postponed by the client or doctor this visit/hospitalization:
None
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 9 of 9
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Monday, June 21, 2021 8:55 AM
Care Provided at
Laurel MD on
Chewy Bear was presented on 8/31/2021 for: Surgery/Anesthesia-Dental Cleaning w/
Comprehensive Exam, pro<3
O aware BW information
Subjective
See 'Plan and Other Notes' section for patient history documentation, if pertinent.
Visit Info: Chewy Bear's visit began at 8:31 AM on 8/31/2021 and ended on 8/31/2021
Doctors Assisting or Consulting with Care:
Medical Authorization Release Signed?
Future appointment(s) scheduled for:
None agreed to by client
Dr. Angelina M Williams
Yes
Patient Information on 8/31/2021
Name: Chewy Bear
Species: Canine
Breed: Terrier, Yorkshire
Gender: Male (Neutered)
Description: brn
Date of Birth: 9/30/2015
Optimum Wellness Plan: Active Care Plus
Microchip #: 985112007160438 Home Again
Chewy Bear has visited this Banfield Hospital 4 times.
Chewy Bear's first visit on 3/15/2021 at this hospital
Chewy Bear's last visit on 8/31/2021 at this hospital
Weight: 25.20 Lbs/11.43 Kgs
Preventive Care Given Due Date Preventive Care Given Due Date
Heartworm Prevention 8/31/2021 3/1/2022 Heartworm Test 8/31/2021 8/31/2022
Flea Prevention 6/21/2021 7/21/2021 Lyme Test 8/31/2021 8/31/2022
Tick Prevention 6/21/2021 7/21/2021 Ehrlichia test 8/31/2021 8/31/2022
Roundworms 8/31/2021 2/27/2022 Anaplasma Test 8/31/2021 8/31/2022
Hookworms 8/31/2021 2/27/2022 Blood Cell Count 8/31/2021 2/27/2022
Rabies 9/2/2020 9/2/2023 Serum Chemistries 8/31/2021 2/27/2022
DAPP 6/21/2021 6/21/2024 Differential Exam 8/31/2021 2/27/2022
Leptospirosis 11/23/2020 11/23/2021 Electrolytes 8/31/2021 8/31/2022
Bordetella 11/23/2020 11/23/2021 Fecal Exam 8/31/2021 2/27/2022
Lyme 11/23/2020 11/23/2021 Urine Specific Gravity 8/31/2021 8/31/2022
Dental Prophylaxis 8/31/2021 8/31/2022 Urine Strip Tests 8/31/2021 8/31/2022
Diphenhydramine 8/31/2021 9/1/2021 Urine Sediment Exam 8/31/2021 8/31/2022
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 1 of 12
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, August 31, 2021 8:31 AM
Care Provided at
Laurel MD on
Abnormal Findings:
Overall Condition Body Condition Score - Above Ideal
Ocular Epiphora on Left Eyelid Epiphora on Right Eyelid
Otic Aberrant Hair - Left Ear Aberrant Hair - Right Ear
Oral/Nasal Tartar on Teeth - Found Swelling/Inflammation of Gums - Found
Normal or Not Selected Findings:
Overall Condition Dehydration Level - No Dehydration
Nutritional Evaluation Complete
Overall Evaluation Complete
Coat and Skin Coat/Skin Normal
Respiratory Respiratory Normal
Cardiovascular Cardiovascular Normal
Abdominal Abdominal Normal
Urogenital Urogenital Normal
Perineal Perineal Normal
Musculoskeletal Musculoskeletal Normal
Neurological Neurological Normal
Laboratory Results: (é = above normal; ê = below normal; ********** = could not be evaluated)
Temperature: 101.5º F - Within Normal Limits
Heart Rate: 116/min - Within Normal Limits
Respiration: 24/min - Within Normal Limits
Capillary Refill Time: Under 2 Seconds
Exam was certified by Dr. Angelina M Williams, DVM on 8/31/2021
Physical Exam Findings on 8/31/2021
Objective
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 2 of 12
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, August 31, 2021 8:31 AM
Care Provided at
Laurel MD on
Recorded on 8/31/2021 10:22:53 AM
Test Name Result Units Range
Fecal - Roundworm Eggs NEGATIVE
Fecal - Hookworm Eggs NEGATIVE
Fecal - Whipworm Eggs NEGATIVE
Fecal - Giardia NEGATIVE
Fecal - Coccidia Oocysts NEGATIVE
Fecal - Tapeworms NEGATIVE
Fecal - Abnormal Bacteria NEGATIVE
Fecal - Significant Blood NEGATIVE
Fecal - 'Other' Eggs NEGATIVE
Recorded on 8/31/2021 1:30:21 PM
Test Name Result Units Range
WBC 9.98 10^9/l (6.000-17.000)
Lymphocyte 2.010 10^9/l (1.000-4.800)
Monocyte 0.45 10^9/l (0.200-1.500)
Neutrophil 7.44 10^9/l (3.000-12.000)
Eosinophil 0.06 10^9/l (0.000-0.800)
Basophil 0.02 10^9/l (0.000-0.400)
Lymphocyte, % 20.2 % (9.000-47.000)
Monocyte, % 4.5 % (2.000-12.000)
Neutrophil, % 74.5 % (42.000-84.000)
Eosinophil, % ê 0.6 % (1.000-18.000)
Basophil, % 0.2 % (0.000-1.100)
RBC Count (RBC) 7.74 10^12/l (5.500-8.500)
Hemoglobin (HGB) 17.5 g/dl (12.000-18.000)
Hematocrit (HCT) 52.73 % (37.000-55.000)
MCV 68.0 fl (60.000-77.000)
MCH 22.6 pg (19.500-24.500)
MCHC 33.2 g/dl (31.000-39.000)
RDW 16.4 % (14.000-20.000)
Platelet Count (PLT) 258.0 10^9/l (165.000-500.000)
PCT 0.3 % (0.150-0.390)
MPV é 11.6 fl (3.900-11.100)
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 3 of 12
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, August 31, 2021 8:31 AM
Care Provided at
Laurel MD on
Recorded on 8/31/2021 1:30:28 PM
Test Name Result Units Range
Electrocardiogram Interpretation NORMAL
Hospital Comments: nsr
Recorded on 8/31/2021 1:30:33 PM
Test Name Result Units Range
Albumin (ALB) 3.5 g/dL (2.300-4.000)
Alkaline Phosphatase (ALKP) ê <10.0 U/L (23.000-212.000)
ALT/SGPT (ALT) 54.0 U/L (10.000-125.000)
BUN (Blood Urea Nitrogen) 11.0 mg/dL (7.000-27.000)
Calcium (CA) 10.4 mg/dL (7.900-12.000)
Cholesterol (CHOL) 268.0 mg/dL (110.000-320.000)
Creatinine (CREA) 1.0 mg/dL (0.500-1.800)
Gamma Glutamyl Transferase (GGT) 0.0 U/L (0.000-11.000)
Globulin (GLOB) 3.5 g/dL (2.500-4.500)
Glucose (GLU) 91.0 mg/dL (74.000-143.000)
Phosphorus (PHOS) 4.6 mg/dL (2.500-6.800)
Bilirubin, Total (TBIL) 0.4 mg/dL (0.000-0.900)
Protein, Total (TP) 7.0 g/dL (5.200-8.200)
ALB/Glob 1.0
BUN/Crea 11.0
Recorded on 8/31/2021 1:30:36 PM
Test Name Result Units Range
Sodium (Na+) 154.0 mmol/L (144.000-160.000)
Potassium (K+) 4.1 mmol/L (3.500-5.800)
Chloride (CL-) 116.0 mmol/L (109.000-122.000)
Na+/K+ 37.0
Osmolality 303.0 mmol/kg
Recorded on 8/31/2021 1:30:41 PM
Test Name Result Units Range
Heartworm (antigen) NEGATIVE
Lyme (antibody) NEGATIVE
Ehrlichia Canis/Ehrlichia Ewingii
(antibody)
NEGATIVE
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 4 of 12
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, August 31, 2021 8:31 AM
Care Provided at
Laurel MD on
Anaplasma
Phagocytophilum/Anaplasma Platys
(antibody)
NEGATIVE
Recorded on 8/31/2021 1:52:06 PM
Test Name Result Units Range
Urine Occult Blood NEGATIVE
Urine Bilirubin NEGATIVE
Urine Urobilinogen 0.0 (0.000-1.000)
Urine Ketone NEGATIVE
Urine Protein 0.0 (0.000-30.000)
Urine Glucose 0.0 (0.000-0.000)
Urine pH 6.0 (5.000-7.500)
Urine Nitrite
Urine Leukocytes
Urine Ascorbic Acid
Hospital Comments: 40
Urine Color NORMAL
Hospital Comments: yellow
Urine Appearance NORMAL
Hospital Comments: clear
Urine Sample Collection Method (Free
catch)
NEGATIVE
Urine Sample Collection Method
(Cystocentesis)
POSITIVE
Urine Sample Collection Method
(Sterile catheter)
NEGATIVE
Recorded on 8/31/2021 1:52:20 PM
Test Name Result Units Range
Urine Specific Gravity 1.032 (1.016-1.080)
Urine Sample Collection Method (Free
catch)
NEGATIVE
Urine Sample Collection Method
(Cystocentesis)
POSITIVE
Urine Sample Collection Method
(Sterile catheter)
NEGATIVE
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 5 of 12
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, August 31, 2021 8:31 AM
Care Provided at
Laurel MD on
Recorded on 8/31/2021 1:52:36 PM
Test Name Result Units Range
Urine WBC NEGATIVE
Urine RBC NEGATIVE
Urine Epithelial Cells NEGATIVE
Urine Bacteria NEGATIVE
Urine Crystals NEGATIVE
Urine Casts NEGATIVE
Urine Sperm NEGATIVE
Urine Sample Collection Method (Free
catch)
NEGATIVE
Urine Sample Collection Method
(Cystocentesis)
POSITIVE
Urine Sample Collection Method
(Sterile catheter)
NEGATIVE
Assessment
Tentative Diagnosis Status Date Hospital Team Member
Dental Calculus Condition Resolved 8/31/2021 1364 Laurel
Epiphora Stable/Persistent/Chronic 8/31/2021 1364 Laurel
Gingivitis Further Defined 8/31/2021 1364 Laurel
Periodontal Disease Stage 2 Stable/Persistent/Chronic 8/31/2021 1364 Laurel
Vomiting, Conservative Condition Resolved 8/31/2021 1364 Laurel
Patella Luxation, Medial, Grade 1 Stable/Persistent/Chronic 3/20/2021 1364 Laurel
Otitis Externa, Medical Undergoing Therapy 9/2/2020 1182 Largo
Dental Calculus Undergoing Therapy 12/14/2019 1182 Largo
Anal Sacs, Full (Otherwise Normal) Needs Protocol 3/9/2019 1182 Largo
Patellar Luxation, Medical Stable/Persistent/Chronic 3/9/2019 1182 Largo
Cystitis Undergoing Therapy 6/11/2018 1006
Calverton
Otitis Externa, Medical Undergoing Therapy 3/3/2018 1006
Calverton
Constipation, Conservative Needs Protocol 11/18/2017 1006
Calverton
Granuloma, Acral Lick Stable/Persistent/Chronic 7/6/2017 1182 Largo
Epiphora Stable/Persistent/Chronic 6/14/2017 1182 Largo
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 6 of 12
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, August 31, 2021 8:31 AM
Care Provided at
Laurel MD on
Patellar Luxation, Medical Needs Protocol 6/14/2017 1182 Largo
Pruritus Undergoing Therapy 6/14/2017 1182 Largo
Dental Calculus Undergoing Therapy 6/8/2017 1006
Calverton
Healthy Pet Needs Protocol 5/31/2017 1182 Largo
Plan and Other Notes
Prescribed and Administered Therapy for this visit/hospitalization:
(Reported by most recent date first)
8/31/2021
Intestinal Parasite Fecal Exam - Completed
Physical Exam: Wellness Plan - Completed
Canine Heartworm/Lyme/Ehrlichia/Anaplasma SNAP Test
- Completed
Comprehensive Exam - Canine - Completed
Exam - Dental - Completed
Otoscopic Exam - Complete - Completed
Dental Prophylaxis Canine Package - Completed
Anesthesia Canine Dental - Completed
Blood Sample Collect / Prep - Completed
Complete Blood Cell Count (CBC/5 part machine
differential) - Completed
Electrocardiogram Monitoring - Completed
Fluid Administration - Lactated Ringers Solution -
Completed
Hospitalization-Hospital Team Care - Completed
Internal Organ Function Screen - Completed
IV Extension Set (Each) - Completed
IV Fluids Pump - Completed
Pre-Med/Induction Injectable - Completed
Pulse Oximeter - Completed
Tracheal Intubation - Completed
Pre-Vaccination Package, High Risk Breed - Completed
Pyrantel Pamoate 50mg/ml (per ml) - Completed
Urine Sample Collect/Prep - Completed
Urine Specific Gravity - Completed
ProHeart 6 (<25lbs) Injection - Completed
Office Visit - Completed
Blood Sample Collect / Prep - Completed
Cerenia 10mg/ml Injectable (per ml) - Completed
Day Care for Optimum Exam - Completed
Ophthalmic Exam - Complete - Completed
Rectal Exam - Brief - Completed
Acepromazine Injectable (per ml) - Completed
Blood Pressure Monitoring, Anesthesia - Completed
Butorphanol 10mg/ml Injectable (per ml) - Completed
Dental Prophylaxis - Completed
Electrolytes (K, Na, Cl, Na/K) - Completed
Hospitalization-Doctor's Supervision - Completed
Hospitalization-Ward Fee - Completed
IV Catheter Insertion - Completed
IV Fluid Administration Set (Each) - Completed
Pre-Anesthetic Examination - Completed
Propofol Injectable (per ml) - Completed
Recovery Care After Anesthesia - Completed
Fecal Sample Collect / Prep - Completed
Diphenhydramine Injection (Pre-Vaccination) -
Completed
Urinalysis Test (Individual) - Completed
Urine Sediment Exam - Completed
Medical Waste Disposal Fee - Completed
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 7 of 12
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, August 31, 2021 8:31 AM
Care Provided at
Laurel MD on
Additional Medical Notes documented for this visit/hospitalization:
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
9/29/2021 2:21 PM
Miscellaneous Johnson-Downes, K. 1364 Laurel
Client inquired re status
Vaccine history sent to email on file as requested by O.
8/31/2021 3:46 PM
Plan Williams, A. Walters, C. Smith, S. 1364 Laurel
ProHeart Administration
Administered at: 08/31/2021 1:43 PM
Lot Number: 457442
Amount Given: 0.57 ml
Site of Administration: Left Front Leg
8/31/2021 1:30 PM
Plan Williams, A. Walters, C. Smith, S. 1364 Laurel
The Lab Results for Complete Blood Cell Count (CBC/5 part machine differential) were manually
entered.
8/31/2021 12:58 PM
Plan Williams, A. Walters, C. Smith, S. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 8/31/2021 Prescription #: 1364-12618545
Rx: Pyrantel Pamoate 50mg/ml (per ml) Manufacturer: Apexa
Instructions: Give 2.5 mls one time
Providing Doctor: Angelina Williams Quantity: 2.50
Discard By: 3/1/2022 Number of Refills: N/A Refill Expiration Date: N/A
8/31/2021 12:58 PM
Plan Williams, A. Walters, C. Smith, S. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 8/31/2021 Prescription #: 1364-12618543
Rx: Diphenhydramine Injection (Pre-Vaccination) Manufacturer:
Instructions: Inject 1 ml one time
Providing Doctor: Angelina Williams Quantity: 1.00
Discard By: 3/1/2022 Number of Refills: 0 Refill Expiration Date: 2/28/2022
8/31/2021 12:58 PM
Plan Williams, A. Walters, C. Smith, S. 1364 Laurel
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 8 of 12
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, August 31, 2021 8:31 AM
Care Provided at
Laurel MD on
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 8/31/2021 Prescription #: 1364-12618542
Rx: Propofol Injectable (per ml) Manufacturer: Abbott
Instructions: Inject 3 mls one time
Providing Doctor: Angelina Williams Quantity: 3.00
Discard By: 3/1/2022 Number of Refills: N/A Refill Expiration Date: N/A
8/31/2021 12:58 PM
Plan Williams, A. Walters, C. Smith, S. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 8/31/2021 Prescription #: 1364-12618539
Rx: Fluid Administration - Lactated Ringers Solution Manufacturer:
Instructions: Administer 6.6 mls one time
Providing Doctor: Angelina Williams Quantity: 6.60
Discard By: 3/1/2022 Number of Refills: N/A Refill Expiration Date: N/A
8/31/2021 12:58 PM
Plan Williams, A. Walters, C. Smith, S. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 8/31/2021 Prescription #: 1364-12618541
Rx: Butorphanol 10mg/ml Injectable (per ml) Manufacturer:
Instructions: Inject 0.3 mls one time
Providing Doctor: Angelina Williams Quantity: 0.30
Discard By: 3/1/2022 Number of Refills: N/A Refill Expiration Date: N/A
8/31/2021 12:58 PM
Plan Williams, A. Walters, C. Smith, S. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 8/31/2021 Prescription #: 1364-12618540
Rx: Acepromazine Injectable (per ml) Manufacturer:
Instructions: Inject 0.1 mls one time
Providing Doctor: Angelina Williams Quantity: 0.10
Discard By: 3/1/2022 Number of Refills: N/A Refill Expiration Date: N/A
8/31/2021 12:58 PM
Plan Williams, A. Walters, C. Smith, S. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 8/31/2021 Prescription #: 1364-12618412
Rx: Cerenia 10mg/ml Injectable (per ml) Manufacturer:
Instructions: Inject 1 ml one time
Providing Doctor: Angelina Williams Quantity: 1.00
Discard By: 3/1/2022 Number of Refills: N/A Refill Expiration Date: N/A
8/31/2021 11:56 AM
Plan Williams, A. Walters, C. Smith, S. 1364 Laurel
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 9 of 12
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, August 31, 2021 8:31 AM
Care Provided at
Laurel MD on
Client notified re status: Pet vomited after surgery, appears to be whole kibbles so we can tell that pt ate
this morning. O. reports that pt sometimes has left overs from the evening portion of food so he may
have eaten this morning. O, approved cerenia inj. Advised o. that pick up time will be closer to 2 pm so
that we can monitor pt throughout recovery and ensure that vomiting has ceased prior to discharge.
AMW
8/31/2021 8:34 AM
Plan Williams, A. Smith, S. 1364 Laurel
Treatment plan for Chewy Bear for $24.05 authorized by Connie Diaz via Phone, on 8/31/2021 8:34
AM. Provider Team Member- Sam
Yes DIP
8/31/2021 8:31 AM
Assessment Smith, S. 1364 Laurel
Epiphora Stable/Persistent/Chronic
Gingivitis Further Defined
Periodontal Disease Stage 2 Stable/Persistent/Chronic
Dental Calculus Condition Resolved
Vomiting, Conservative Condition Resolved
8/31/2021 8:31 AM
Objective Smith, S. 1364 Laurel
8/31/2021 8:31 AM
Plan(Notes) Williams, A. Walters, C. Smith, S. 1364 Laurel
Routine dentistry:
___Chewy Bear___has:
Generalized mild plaque.
Generalized mild calculus.
Recommendations:Daily brushing, CET chews, or Greenies
Complete dental prophylaxis: yes
Home dental care:
----------------------------------------------------
Examination Notes.
S: Pet presented for dental cleaning. O noted the patient is always stretching with the hind left leg. No
other concerns noted at this time.
O: BARH, TPR-wnl, MM pink/moist, CRT <2 sec, dental calculus/gingivitis,
EENT: epiphora AU, ears - aberrant hair AU, abd pal:wnl, heart and lung sounds:wnl, ms:wnl,
skin:wnl
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 10 of 12
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, August 31, 2021 8:31 AM
Care Provided at
Laurel MD on
A: Dental calc -resolved
P: Exam
UA:
fecal:
4Dx: neg
pyrantel (50 mg/ml) 2.5 ml PO TGH
diphenhydramine inj (50 mg/ml) 0.5 ml IM prior to vax
Proheart Inj (0.0227 ml/lb) 0.57 ml SQ
CBC/Chemistry/Electrolytes:
IV catheter/fluids (LRS) @ 40ml/hr throughout procedure. Total: 6.6ml
Dental Prophy
Admin 1.0ml cerenia SC @ 11:59a
Premed: Butorphanol (10mg/ml) 0.3ml/Acepromazine (1mg/ml) 0.1ml IM at 10:59a. P returned to
kennel.
Induction: Inserted size _22 g_ catheter into _RF_ leg. Administered 3.0 ml Propofol (10mg/ml).
Maintenance: Inserted size 7.0 Endotracheal tube. Sevofluorane gas.
Sx:Monitored pet with ECG, and Pulse OX. Administered fluids of LRS at 40ml/hr. Routine dental prophy
performed. Returned to kennel, extubated, and monitored until discharge without complications.
Removed catheter at time of discharge.
Rx:
1 Prognosis: Good
2 Client Education: Exam findings. Test results. Recommend monthly F/T/HW prevention. Monitor P
closely this evening since she was under anesthesia today. Offer food this evening or early tomorrow
morning. P may be lethargic up to 48 hours after the anesthetic procedure. P may have mild nausea
and/or mild loose stools after the anesthetic procedure.
3 Recheck: 3 mo
4 Follow-Up Therapy: lepto, bord, lyme
Team Member: Dr. W/CW/SKM
-----------------------------------------------------------------------------
Anesthesia Machine Checklist performed by CW/SKM; Confirmed by Dr. Williams
ANESTHESIA
Cuff Appropriately Inflated and Pressure Checked: __x_ Yes ___ No
Pre-Induction T:100.0 P:130 R:28
MAINTENANCE / MONITORING -
Time: 11:30 11:33 11:38
__x__ Sevo % -> 3 2.5 2.5
__x__ Oxygen Flow (L/min) -> 3 2 2
__x_ Heart Rate -> 124 118 129
__x__ Pulse Ox O2 -> 98 98 98
__x__ Respiratory Rate -> 24 28 28
__x__ CRT/memb. Color -> p/<2 p/<2 p/<2
__x__ Pulse Quality -> gd gd gd
__x__ ECG rhythm -> NSR NSR NSR
__x__ BP-> 107/61/76 94/63/73 92/55/67
__x__ Temperature-> 99.9 99.9 99.9
Post-operative T:99.9 P:129 R:28
EQUIPMENT
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 11 of 12
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, August 31, 2021 8:31 AM
Care Provided at
Laurel MD on
Vaporizer Type: Vasco Anesthesia Machine Type: Vasco
Breathing Circuit: ____ Nonrebreathing __x__ Rebreathing
System Leak Test Performed: __x__Yes ____ No
Absorber Type: Sodalime
Discharge TPR performed by CW/SKM: wnl
***********************************************************************
8/31/2021 8:31 AM
Subjective Williams, A. Smith, S. 1364 Laurel
always left back leg when stretching
Home Care Instructions documented for this visit/hospitalization:
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
None
Therapy presented & declined by the client for this visit/ hospitalization:
None
Therapy considered but not medically necessary for this visit/hospitalization:
None
Therapy postponed by the client or doctor this visit/hospitalization:
None
Time Printed: 1:16 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 12 of 12
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, August 31, 2021 8:31 AM
Care Provided at
Laurel MD on
Chewy Bear was presented on 10/19/2021 for: Illness-Coat/Skin, bump on tail
Subjective
See 'Plan and Other Notes' section for patient history documentation, if pertinent.
Visit Info: Chewy Bear's visit began at 8:54 AM on 10/19/2021 and ended on 10/19/2021
Doctors Assisting or Consulting with Care:
Medical Authorization Release Signed?
Future appointment(s) scheduled for:
None agreed to by client
Dr. Jamila Y Echols, Dr. Sabrina Owens
Yes
Patient Information on 10/19/2021
Name: Chewy Bear
Species: Canine
Breed: Terrier, Yorkshire
Gender: Male (Neutered)
Description: brn
Date of Birth: 9/30/2015
Optimum Wellness Plan: Active Care Plus
Microchip #: 985112007160438 Home Again
Chewy Bear has visited this Banfield Hospital 5 times.
Chewy Bear's first visit on 3/15/2021 at this hospital
Chewy Bear's last visit on 10/19/2021 at this hospital
Weight: 25.80 Lbs/11.70 Kgs
Preventive Care Given Due Date Preventive Care Given Due Date
Heartworm Prevention 8/31/2021 3/1/2022 Heartworm Test 8/31/2021 8/31/2022
Flea Prevention 10/19/2021 4/17/2022 Lyme Test 8/31/2021 8/31/2022
Tick Prevention 10/19/2021 4/17/2022 Ehrlichia test 8/31/2021 8/31/2022
Roundworms 8/31/2021 2/27/2022 Anaplasma Test 8/31/2021 8/31/2022
Hookworms 8/31/2021 2/27/2022 Blood Cell Count 8/31/2021 2/27/2022
Rabies 9/2/2020 9/2/2023 Serum Chemistries 8/31/2021 2/27/2022
DAPP 6/21/2021 6/21/2024 Differential Exam 8/31/2021 2/27/2022
Leptospirosis 11/23/2020 11/23/2021 Electrolytes 8/31/2021 8/31/2022
Bordetella 11/23/2020 11/23/2021 Fecal Exam 8/31/2021 2/27/2022
Lyme 11/23/2020 11/23/2021 Urine Specific Gravity 8/31/2021 8/31/2022
Dental Prophylaxis 8/31/2021 8/31/2022 Urine Strip Tests 8/31/2021 8/31/2022
Diphenhydramine 8/31/2021 9/1/2021 Urine Sediment Exam 8/31/2021 8/31/2022
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 1 of 5
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, October 19, 2021 8:54 AM
Care Provided at
Laurel MD on
Abnormal Findings:
Overall Condition Body Condition Score - Above Ideal
Ocular Epiphora on Left Eyelid Epiphora on Right Eyelid
Otic Aberrant Hair - Left Ear Aberrant Hair - Right Ear
Oral/Nasal Tartar on Teeth - Found Swelling/Inflammation of Gums - Found
Normal or Not Selected Findings:
Overall Condition Nutritional Evaluation Complete Overall Evaluation Complete
Coat and Skin Coat/Skin Normal
Respiratory Respiratory Normal
Cardiovascular Cardiovascular Normal
Abdominal Abdominal Normal
Urogenital Urogenital Normal
Perineal Perineal Normal
Musculoskeletal Musculoskeletal Normal
Neurological Neurological Normal
Temperature: 101º F -
Heart Rate: 138/min -
Respiration: Unable To Evaluate
Capillary Refill Time: Under 2 Seconds
Exam was certified by Dr. Jamila Y Echols, DVM on 10/19/2021
Physical Exam Findings on 10/19/2021
Objective
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 2 of 5
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, October 19, 2021 8:54 AM
Care Provided at
Laurel MD on
Additional Medical Notes documented for this visit/hospitalization:
(Reported by most recent date first)
Assessment
Tentative Diagnosis Status Date Hospital Team Member
Anal Sacs, Full (Otherwise Normal) Condition Resolved 10/19/2021 1364 Laurel
Epiphora Stable/Persistent/Chronic 10/19/2021 1364 Laurel
Periodontal Disease Stage 2 Stable/Persistent/Chronic 10/19/2021 1364 Laurel
Patella Luxation, Medial, Grade 1 Stable/Persistent/Chronic 3/20/2021 1364 Laurel
Otitis Externa, Medical Undergoing Therapy 9/2/2020 1182 Largo
Dental Calculus Undergoing Therapy 12/14/2019 1182 Largo
Anal Sacs, Full (Otherwise Normal) Needs Protocol 3/9/2019 1182 Largo
Patellar Luxation, Medical Stable/Persistent/Chronic 3/9/2019 1182 Largo
Cystitis Undergoing Therapy 6/11/2018 1006
Calverton
Otitis Externa, Medical Undergoing Therapy 3/3/2018 1006
Calverton
Constipation, Conservative Needs Protocol 11/18/2017 1006
Calverton
Granuloma, Acral Lick Stable/Persistent/Chronic 7/6/2017 1182 Largo
Epiphora Stable/Persistent/Chronic 6/14/2017 1182 Largo
Patellar Luxation, Medical Needs Protocol 6/14/2017 1182 Largo
Pruritus Undergoing Therapy 6/14/2017 1182 Largo
Dental Calculus Undergoing Therapy 6/8/2017 1006
Calverton
Healthy Pet Needs Protocol 5/31/2017 1182 Largo
Plan and Other Notes
Prescribed and Administered Therapy for this visit/hospitalization:
(Reported by most recent date first)
10/19/2021
Office Visit - Completed
Ear Cleaning Level 1 - Completed
Express Anal Glands - Completed
Physical Exam: Wellness Plan - Completed
Ear Hair Removal - Completed
Simparica Blue (22.1-44lbs) Card 6ct - Completed
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 3 of 5
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, October 19, 2021 8:54 AM
Care Provided at
Laurel MD on
Date Type Note Doctor VT/VA CSC Hospital
10/19/2021 11:34 AM
Miscellaneous Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Called client (connie) and lvm letting her know that P is ready to be picked up. -AR
10/19/2021 10:10 AM
Plan Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 10/19/2021 Prescription #: 1364-12655140
Rx: Simparica Blue (22.1-44lbs) Card 6ct Manufacturer: Zoetis
Instructions: Give 1 chewable tablet every 30 days until gone
Providing Doctor: Jamila Echols Quantity: 1.00
Discard By: 4/19/2022 Number of Refills: 0 Refill Expiration Date: 4/19/2022
10/19/2021 8:55 AM
Assessment Echols, J. Rey, A. Entzminger, E. 1364 Laurel
PD2
Epiphora
Full Anal Glands
Epiphora Stable/Persistent/Chronic
Periodontal Disease Stage 2 Stable/Persistent/Chronic
Anal Sacs, Full (Otherwise Normal) Condition Resolved
10/19/2021 8:55 AM
Objective Echols, J. Rey, A. Entzminger, E. 1364 Laurel
BARH, TPR-wnl, MM pink/moist, CRT <2 sec, dental calculus/gingivitis,
EENT: epiphora AU, ears - aberrant hair AU, abd pal:wnl, heart and lung sounds:wnl, ms:wnl,
skin:wnl
10/19/2021 8:55 AM
Plan(Notes) Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Physical Exam
Ear Cleaning
Ear Hair Removal
Anal Gland Expression
1. Prognosis: Good with recommendations, treatment, and owner compliance
2. Client Education: flea/tick and HW prevention, vaccine schedule, vaccine reactions
3. Recheck: 1 month
4. Follow up therapy: vaccines
**********************************************
10/19/2021 8:55 AM
Subjective Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 4 of 5
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, October 19, 2021 8:54 AM
Care Provided at
Laurel MD on
P presents for exam. Client states they felt a bump under his tail but it has gotten better and believes it
could just be his anal glands. O approved anal gland expression. Client also had a concern about P
licking his penis for a long time, it has only happened once. Client states she hasn't paid attention to P's
urinating habits and states that P is good at holding it in and letting the owner know when he really has
to go.
Home Care Instructions documented for this visit/hospitalization:
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
None
Therapy presented & declined by the client for this visit/ hospitalization:
Cytology Collect / Prep for Reflab - Client Declines
Simparica Blue (22.1-44lbs) Single Dose - Client Declines
Urinalysis Test (Individual) - Client Declines
Urine Sediment Exam - Client Declines
Cytology ( 1 organ, 1 site) - RefLab (ES) - Client Declines
Urinalysis Testing and Collection Package - Client Declines
Urine Specific Gravity - Client Declines
Urine Sample Collect/Prep - Client Declines
Therapy considered but not medically necessary for this visit/hospitalization:
Medical Waste Disposal Fee - Not Medically Necessary Medical Waste Disposal Fee - Not Medically Necessary
Therapy postponed by the client or doctor this visit/hospitalization:
None
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 5 of 5
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, October 19, 2021 8:54 AM
Care Provided at
Laurel MD on
Chewy Bear was presented on 3/8/2022 for: Preventive Care-Vaccination/Deworming,
proheart
Subjective
See 'Plan and Other Notes' section for patient history documentation, if pertinent.
Visit Info: Chewy Bear's visit began at 9:10 AM on 3/8/2022 and ended on 3/8/2022
Doctors Assisting or Consulting with Care:
Medical Authorization Release Signed?
Future appointment(s) scheduled for:
None agreed to by client
Dr. Sabrina Owens
Yes
Patient Information on 3/8/2022
Name: Chewy Bear
Species: Canine
Breed: Terrier, Yorkshire
Gender: Male (Neutered)
Description: brn
Date of Birth: 9/30/2015
Optimum Wellness Plan: Active Care Plus
Microchip #: 985112007160438 Home Again
Chewy Bear has visited this Banfield Hospital 7 times.
Chewy Bear's first visit on 3/15/2021 at this hospital
Chewy Bear's last visit on 3/8/2022 at this hospital
Weight: 29.06 Lbs/13.18 Kgs
Preventive Care Given Due Date Preventive Care Given Due Date
Heartworm Prevention 3/8/2022 9/6/2022 Heartworm Test 8/31/2021 8/31/2022
Flea Prevention 10/19/2021 4/17/2022 Lyme Test 8/31/2021 8/31/2022
Tick Prevention 10/19/2021 4/17/2022 Ehrlichia test 8/31/2021 8/31/2022
Roundworms 2/22/2022 8/21/2022 Anaplasma Test 8/31/2021 8/31/2022
Hookworms 2/22/2022 8/21/2022 Blood Cell Count 2/22/2022 8/21/2022
Rabies 9/2/2020 9/2/2023 Serum Chemistries 2/22/2022 8/21/2022
DAPP 6/21/2021 6/21/2024 Differential Exam 2/22/2022 8/21/2022
Leptospirosis 2/22/2022 2/22/2023 Electrolytes 2/22/2022 2/22/2023
Bordetella 2/22/2022 2/22/2023 Fecal Exam 2/22/2022 8/21/2022
Lyme 2/22/2022 2/22/2023 Urine Specific Gravity 8/31/2021 8/31/2022
Dental Prophylaxis 2/22/2022 2/22/2023 Urine Strip Tests 8/31/2021 8/31/2022
Diphenhydramine 3/8/2022 3/9/2022 Urine Sediment Exam 8/31/2021 8/31/2022
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 1 of 6
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, March 8, 2022 9:10 AM
Care Provided at
Laurel MD on
Abnormal Findings:
Overall Condition Body Condition Score - Overweight
Laboratory Results: (é = above normal; ê = below normal; ********** = could not be evaluated)
Recorded on 3/8/2022 12:57:25 PM
Test Name Result Units Range
Total T4 2.2 μg/dL (1.000-4.000)
Interpretive Guidelines Diagnostic Interpretation for TT4 < 1.0 μg/dL Low 1.0 - 2.0 μg/dL Low
Normal 1.0 - 4.0 μg/dL Normal > 4.0 μg/dL High 2.1 - 5.4 μg/dL
Therapeutic Dogs with no clinical signs of hypothyroidism and results within
the normal reference range are likely euthyroid. Dogs with low T4
concentrations may be hypothyroid or "euthyroid sick". Occasionally,
hypothyroid dogs can have T4 concentrations that are low normal. Dogs with
clinical signs of hypothyroidism and low or low normal T4 concentrations may
be evaluated further by submission of freeT4 (fT4) and canine TSH. A high T4
concentration in a clinically normal dog is likely a variation of normal; however
elevations may occur secondary to thyroid auto antibodies or rarely thyroid
neoplasia. For dogs on thyroid supplement, acceptable 4-6 hour post pill total
T4 concentrations generally fall within the higher end or slightly above the
reference range.
Assessment
Tentative Diagnosis Status Date Hospital Team Member
Overweight Stable/Persistent/Chronic 3/8/2022 1364 Laurel
Epiphora Stable/Persistent/Chronic 2/22/2022 1364 Laurel
Temperature: 101.2º F - Within Normal Limits
Heart Rate: 140/min - Within Normal Limits
Respiration: Unable To Evaluate
Capillary Refill Time: Under 2 Seconds
Exam was certified by Dr. Sabrina Owens, DVM on 3/8/2022
Physical Exam Findings on 3/8/2022
Objective
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 2 of 6
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, March 8, 2022 9:10 AM
Care Provided at
Laurel MD on
Additional Medical Notes documented for this visit/hospitalization:
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
5/31/2022 3:49 PM
Miscellaneous Hamilton, S. 1364 Laurel
Periodontal Disease Stage 2 Stable/Persistent/Chronic 2/22/2022 1364 Laurel
Patella Luxation, Medial, Grade 1 Stable/Persistent/Chronic 3/20/2021 1364 Laurel
Otitis Externa, Medical Undergoing Therapy 9/2/2020 1182 Largo
Dental Calculus Undergoing Therapy 12/14/2019 1182 Largo
Anal Sacs, Full (Otherwise Normal) Needs Protocol 3/9/2019 1182 Largo
Patellar Luxation, Medical Stable/Persistent/Chronic 3/9/2019 1182 Largo
Cystitis Undergoing Therapy 6/11/2018 1006
Calverton
Otitis Externa, Medical Undergoing Therapy 3/3/2018 1006
Calverton
Constipation, Conservative Needs Protocol 11/18/2017 1006
Calverton
Granuloma, Acral Lick Stable/Persistent/Chronic 7/6/2017 1182 Largo
Epiphora Stable/Persistent/Chronic 6/14/2017 1182 Largo
Patellar Luxation, Medical Needs Protocol 6/14/2017 1182 Largo
Pruritus Undergoing Therapy 6/14/2017 1182 Largo
Dental Calculus Undergoing Therapy 6/8/2017 1006
Calverton
Healthy Pet Needs Protocol 5/31/2017 1182 Largo
Plan and Other Notes
Prescribed and Administered Therapy for this visit/hospitalization:
(Reported by most recent date first)
3/8/2022
Office Visit - Completed
Pre-Vaccination Package, High Risk Breed - Completed
ProHeart 6 (<25lbs) Injection - Completed
MRX Hills Canine r/d - Completed
Blood Sample Collect / Prep - Completed
Physical Exam: Wellness Plan - Completed
Diphenhydramine Injection (Pre-Vaccination) -
Completed
Medical Waste Disposal Fee - Completed
MRX RC Canine Satiety Treats - Completed
Thyroid Screen (Total T4) - Completed
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 3 of 6
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, March 8, 2022 9:10 AM
Care Provided at
Laurel MD on
Approved from chewy Health for:
MRX hills Prescription diet Metabolic Chicken Flavor Wet Dog food, 13-oz case of 12
Refills:
Approved from chewy Health for:
MRX Hills Canine r/d Weight Reduction Chicken Flavor Dry Dog Food, 8.5-lb bag
Refills:
3/9/2022 2:59 PM
Miscellaneous Hamilton, S. 1364 Laurel
Approved For:
Royal Canin Veterinary Diet Satiety Crunchy Dog treats, 17.6-oz bag
Refills: PRN
3/8/2022 2:13 PM
Plan Owens, S. Johnson-Downes, K. Entzminger, E. 1364 Laurel
ProHeart Administration
Administered at: 03/08/2022 9:53 AM
Lot Number: 473925
Amount Given: 0.65 ml
Site of Administration: Left Front Leg
Route: Subcutaneous Injection
3/8/2022 11:07 AM
Plan Owens, S. Johnson-Downes, K. Entzminger, E. 1364 Laurel
Treatment plan for Chewy Bear for $69.90 authorized by Nelly Diaz via Phone, on 3/8/2022 11:07 AM.
Provider Team Member- Joplin Onderdonk
3/8/2022 11:01 AM
Plan Owens, S. Johnson-Downes, K. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 3/8/2022 Prescription #: 1364-12765699
Rx: MRX RC Canine Satiety Treats Manufacturer:
Instructions:
Providing Doctor: Sabrina Owens Quantity: 1.00
Discard By: N/A Number of Refills: N/A Refill Expiration Date: N/A
3/8/2022 11:01 AM
Plan Owens, S. Johnson-Downes, K. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 3/8/2022 Prescription #: 1364-12765681
Rx: MRX Hills Canine r/d Manufacturer:
Instructions:
Providing Doctor: Sabrina Owens Quantity: 1.00
Discard By: N/A Number of Refills: N/A Refill Expiration Date: N/A
3/8/2022 9:53 AM
Plan Owens, S. Johnson-Downes, K. Entzminger, E. 1364 Laurel
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 4 of 6
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, March 8, 2022 9:10 AM
Care Provided at
Laurel MD on
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 3/8/2022 Prescription #: 1364-12765597
Rx: Diphenhydramine Injection (Pre-Vaccination) Manufacturer:
Instructions: Inject 0.58 mls one time
Providing Doctor: Sabrina Owens Quantity: 1.00
Discard By: 9/6/2022 Number of Refills: N/A Refill Expiration Date: N/A
3/8/2022 9:10 AM
Assessment Owens, S. Johnson-Downes, K. Entzminger, E. 1364 Laurel
Overweight Stable/Persistent/Chronic r/o Hypothyroid
3/8/2022 9:10 AM
Objective Owens, S. Johnson-Downes, K. Entzminger, E. 1364 Laurel
TPR within normal limits. BAR. wt:29.06 # /13.18kg
NT: mm pink, moist, CRT < 2 sec. Normal adult dentition clean
Eyes: wnl
Ears: wnl
PLN: no lymphadenopathy appreciated
H/L: wnl
Abd: soft non painful
Integ: wnl
BCS: 6-7/9
Rest of PE NSF
3/8/2022 9:10 AM
Plan(Notes) Owens, S. Johnson-Downes, K. Entzminger, E. 1364 Laurel
Exam
T4: wnl, 2.2 ug/dL
diphenhydramine inj (50 mg/ml) 0.58 ml IM prior to vax
Proheart Inj (0.0227 ml/lb) 0.65 ml SQ
Take Home: Food card RC's Satiety
1 Prognosis: good with owner compliance
2 Client Education: Continue flea tick and heartworm preventative. Discussed vaccine schedule and
vaccine reactions. Keep Chewy Bear on a good weight loss adult diet consisting of dry kibble and
occasional wet food. I recommend Hill's Science Diet r/d. No treats or table food. I have provided a food
card and treat card for weight loss. I recommend that we do a thyroid screen to rule out
Hypothyroidism as a cause of his continuous weight gain. Thyroid screen was normal so we need to
focus on weight loss and strict diet is important. His teeth look great and I recommend at home dental
care. Options include: brushing teeth, dental chews, and/or water additives. Please give us a call if you
have any questions or concerns.
3 Recheck: 1 month
4 Follow-Up Therapy: weight (outpatient)
***********************************************************************
3/8/2022 9:10 AM
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 5 of 6
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, March 8, 2022 9:10 AM
Care Provided at
Laurel MD on
Subjective Owens, S. Johnson-Downes, K. Entzminger, E. 1364 Laurel
P presents for proheart inj. No health concerns indicated at this time. Feeding RC GI diet.
Home Care Instructions documented for this visit/hospitalization:
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
None
Therapy presented & declined by the client for this visit/ hospitalization:
Internal Organ Function Screen - Client Declines
Therapy considered but not medically necessary for this visit/hospitalization:
None
Therapy postponed by the client or doctor this visit/hospitalization:
None
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 6 of 6
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, March 8, 2022 9:10 AM
Care Provided at
Laurel MD on
Chewy Bear was presented on 9/7/2022 for: Preventive Care-Comprehensive Exam, routine
bw/hwp
Subjective
See 'Plan and Other Notes' section for patient history documentation, if pertinent.
Visit Info: Chewy Bear's visit began at 9:07 AM on 9/7/2022 and ended on 9/7/2022
Doctors Assisting or Consulting with Care:
Medical Authorization Release Signed?
Future appointment(s) scheduled for:
None agreed to by client
Dr. Susan Jones
Yes
Patient Information on 9/7/2022
Name: Chewy Bear
Species: Canine
Breed: Terrier, Yorkshire
Gender: Male (Neutered)
Description: brn
Date of Birth: 9/30/2015
Optimum Wellness Plan: Active Care Plus
Microchip #: 985112007160438 Home Again
Chewy Bear has visited this Banfield Hospital 8 times.
Chewy Bear's first visit on 3/15/2021 at this hospital
Chewy Bear's last visit on 9/7/2022 at this hospital
Weight: 29.40 Lbs/13.34 Kgs
Preventive Care Given Due Date Preventive Care Given Due Date
Heartworm Prevention 9/7/2022 3/8/2023 Heartworm Test 9/7/2022 9/7/2023
Flea Prevention 6/16/2022 12/13/2022 Lyme Test 9/7/2022 9/7/2023
Tick Prevention 6/16/2022 12/13/2022 Ehrlichia test 9/7/2022 9/7/2023
Roundworms 9/7/2022 3/6/2023 Anaplasma Test 9/7/2022 9/7/2023
Hookworms 9/7/2022 3/6/2023 Blood Cell Count 9/7/2022 3/6/2023
Rabies 9/2/2020 9/2/2023 Serum Chemistries 9/7/2022 3/6/2023
DAPP 6/21/2021 6/21/2024 Differential Exam 9/7/2022 3/6/2023
Leptospirosis 2/22/2022 2/22/2023 Electrolytes 2/22/2022 2/22/2023
Bordetella 2/22/2022 2/22/2023 Fecal Exam 9/7/2022 3/6/2023
Lyme 2/22/2022 2/22/2023 Urine Specific Gravity 9/7/2022 9/7/2023
Dental Prophylaxis 2/22/2022 2/22/2023 Urine Strip Tests 9/7/2022 9/7/2023
Diphenhydramine 9/7/2022 9/8/2022 Urine Sediment Exam 9/7/2022 9/7/2023
Time Printed: 1:18 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 1 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Wednesday, September 7, 2022 9:07 AM
Care Provided at
Laurel MD on
Abnormal Findings:
Overall Condition Body Condition Score - Above Ideal
Otic Aberrant Hair - Right Ear
Brown Exudate - Right Ear
Aberrant Hair - Left Ear
Brown Exudate - Left Ear
Oral/Nasal Discoloration of Teeth - Found
Normal or Not Selected Findings:
Overall Condition Diet Recommended - R/D
Dehydration Level - No Dehydration
Overall Evaluation Complete
Nutritional Evaluation Complete
Overall Condition - Good
Coat and Skin Coat/Skin Normal
Ocular Ocular Normal
Respiratory Respiratory Normal
Cardiovascular Cardiovascular Normal
Abdominal Abdominal Normal
Urogenital Urogenital Normal
Perineal Perineal Normal
Musculoskeletal Musculoskeletal Normal
Neurological Neurological Normal
Temperature: 100.1º F - Within Normal Limits
Heart Rate: 148/min - Within Normal Limits
Respiration: Unable To Evaluate
Capillary Refill Time: Under 2 Seconds
Exam was certified by Dr. Susan Jones, DVM on 9/7/2022
Physical Exam Findings on 9/7/2022
Objective
Time Printed: 1:18 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 2 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Wednesday, September 7, 2022 9:07 AM
Care Provided at
Laurel MD on
Laboratory Results: (é = above normal; ê = below normal; ********** = could not be evaluated)
Recorded on 9/7/2022 10:55:19 AM
Test Name Result Units Range
Fecal - Roundworm Eggs NEGATIVE
Fecal - Hookworm Eggs NEGATIVE
Fecal - Whipworm Eggs NEGATIVE
Fecal - Giardia NEGATIVE
Fecal - Coccidia Oocysts NEGATIVE
Fecal - Tapeworms NEGATIVE
Fecal - Abnormal Bacteria NEGATIVE
Fecal - Significant Blood NEGATIVE
Fecal - 'Other' Eggs NEGATIVE
Recorded on 9/7/2022 11:19:39 AM
Test Name Result Units Range
Albumin (ALB) 3.3 g/dL (2.300-4.000)
Alkaline Phosphatase (ALKP) ê <10.0 U/L (23.000-212.000)
ALT/SGPT (ALT) 81.0 U/L (10.000-125.000)
BUN (Blood Urea Nitrogen) 12.0 mg/dL (7.000-27.000)
Calcium (CA) 10.3 mg/dL (7.900-12.000)
Cholesterol (CHOL) 238.0 mg/dL (110.000-320.000)
Creatinine (CREA) 0.7 mg/dL (0.500-1.800)
Gamma Glutamyl Transferase (GGT) 0.0 U/L (0.000-11.000)
Globulin (GLOB) 4.5 g/dL (2.500-4.500)
Glucose (GLU) 109.0 mg/dL (74.000-143.000)
Phosphorus (PHOS) 4.7 mg/dL (2.500-6.800)
Bilirubin, Total (TBIL) 0.9 mg/dL (0.000-0.900)
Protein, Total (TP) 7.8 g/dL (5.200-8.200)
ALB/Glob 0.7
BUN/Crea 17.0
Recorded on 9/7/2022 11:19:48 AM
Test Name Result Units Range
WBC 15.98 10^9/l (6.000-17.000)
Lymphocyte 3.81 10^9/l (1.000-4.800)
Time Printed: 1:18 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 3 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Wednesday, September 7, 2022 9:07 AM
Care Provided at
Laurel MD on
Monocyte 1.39 10^9/l (0.200-1.500)
Neutrophil 10.63 10^9/l (3.000-12.000)
Eosinophil 0.140 10^9/l (0.000-0.800)
Basophil 0.02 10^9/l (0.000-0.400)
Lymphocyte, % 23.8 % (9.000-47.000)
Monocyte, % 8.7 % (2.000-12.000)
Neutrophil, % 66.5 % (42.000-84.000)
Eosinophil, % ê 0.9 % (1.000-18.000)
Basophil, % 0.1 % (0.000-1.100)
RBC Count (RBC) 7.51 10^12/l (5.500-8.500)
Hemoglobin (HGB) é 18.3 g/dl (12.000-18.000)
Hematocrit (HCT) 49.87 % (37.000-55.000)
MCV 66.0 fl (60.000-77.000)
MCH 24.3 pg (19.500-24.500)
MCHC 36.7 g/dl (31.000-39.000)
RDW 16.8 % (14.000-20.000)
Platelet Count (PLT) ê 123.0 10^9/l (165.000-500.000)
PCT ê 0.13 % (0.150-0.390)
MPV 10.7 fl (3.900-11.100)
Recorded on 9/7/2022 11:19:59 AM
Test Name Result Units Range
Heartworm (antigen) NEGATIVE
Lab Comments: View your results in VetConnect Plus for patient-specific interpretations that
incorporate clinical signs.
Lyme (antibody) NEGATIVE
Lab Comments: View your results in VetConnect Plus for patient-specific interpretations that
incorporate clinical signs.
Ehrlichia Canis/Ehrlichia Ewingii
(antibody)
NEGATIVE
Lab Comments: View your results in VetConnect Plus for patient-specific interpretations that
incorporate clinical signs.
Anaplasma
Phagocytophilum/Anaplasma Platys
(antibody)
NEGATIVE
Lab Comments: View your results in VetConnect Plus for patient-specific interpretations that
incorporate clinical signs.
Time Printed: 1:18 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 4 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Wednesday, September 7, 2022 9:07 AM
Care Provided at
Laurel MD on
Recorded on 9/7/2022 5:54:18 PM
Test Name Result Units Range
Ear Swab Yeast POSITIVE
Hospital Comments: AS: scattered yeast
Ear Swab Bacteria NEGATIVE
Ear Swab Mites NEGATIVE
Recorded on 9/7/2022 5:55:55 PM
Test Name Result Units Range
Urine Occult Blood NEGATIVE
Urine Bilirubin NEGATIVE
Urine Urobilinogen 0.0 (0.000-1.000)
Urine Ketone NEGATIVE
Urine Protein 15.0 (0.000-30.000)
Urine Glucose 0.0 (0.000-0.000)
Urine pH 6.0 (5.000-7.500)
Urine Nitrite
Urine Leukocytes
Urine Ascorbic Acid
Hospital Comments: 40
Urine Color NORMAL
Hospital Comments: YELLOW
Urine Appearance NORMAL
Hospital Comments: slightly hazy
Urine Sample Collection Method (Free
catch)
POSITIVE
Urine Sample Collection Method
(Cystocentesis)
NEGATIVE
Urine Sample Collection Method
(Sterile catheter)
NEGATIVE
Recorded on 9/7/2022 5:56:39 PM
Test Name Result Units Range
Urine Specific Gravity 1.055 (1.016-1.080)
Urine Sample Collection Method (Free
catch)
POSITIVE
Time Printed: 1:18 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 5 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Wednesday, September 7, 2022 9:07 AM
Care Provided at
Laurel MD on
Urine Sample Collection Method
(Cystocentesis)
NEGATIVE
Urine Sample Collection Method
(Sterile catheter)
NEGATIVE
Recorded on 9/7/2022 5:58:15 PM
Test Name Result Units Range
Urine WBC NEGATIVE
Urine RBC NEGATIVE
Urine Epithelial Cells POSITIVE
Hospital Comments: occasional epi cells
Urine Bacteria NEGATIVE
Hospital Comments: mild stain debris
Urine Crystals NEGATIVE
Urine Casts NEGATIVE
Urine Sperm NEGATIVE
Urine Sample Collection Method (Free
catch)
POSITIVE
Urine Sample Collection Method
(Cystocentesis)
NEGATIVE
Urine Sample Collection Method
(Sterile catheter)
NEGATIVE
Assessment
Tentative Diagnosis Status Date Hospital Team Member
Anal Sacs, Full (Otherwise Normal) Condition Resolved 9/7/2022 1364 Laurel
Otitis Externa, Medical Undergoing Therapy 9/7/2022 1364 Laurel
Overweight Stable/Persistent/Chronic 9/7/2022 1364 Laurel
Patella Luxation, Medial, Grade 1 Client Postponed 9/7/2022 1364 Laurel
Epiphora Stable/Persistent/Chronic 2/22/2022 1364 Laurel
Periodontal Disease Stage 2 Stable/Persistent/Chronic 2/22/2022 1364 Laurel
Patella Luxation, Medial, Grade 1 Stable/Persistent/Chronic 3/20/2021 1364 Laurel
Otitis Externa, Medical Undergoing Therapy 9/2/2020 1182 Largo
Dental Calculus Undergoing Therapy 12/14/2019 1182 Largo
Anal Sacs, Full (Otherwise Normal) Needs Protocol 3/9/2019 1182 Largo
Patellar Luxation, Medical Stable/Persistent/Chronic 3/9/2019 1182 Largo
Time Printed: 1:18 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 6 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Wednesday, September 7, 2022 9:07 AM
Care Provided at
Laurel MD on
Additional Medical Notes documented for this visit/hospitalization:
Cystitis Undergoing Therapy 6/11/2018 1006
Calverton
Otitis Externa, Medical Undergoing Therapy 3/3/2018 1006
Calverton
Constipation, Conservative Needs Protocol 11/18/2017 1006
Calverton
Granuloma, Acral Lick Stable/Persistent/Chronic 7/6/2017 1182 Largo
Epiphora Stable/Persistent/Chronic 6/14/2017 1182 Largo
Patellar Luxation, Medical Needs Protocol 6/14/2017 1182 Largo
Pruritus Undergoing Therapy 6/14/2017 1182 Largo
Dental Calculus Undergoing Therapy 6/8/2017 1006
Calverton
Healthy Pet Needs Protocol 5/31/2017 1182 Largo
Plan and Other Notes
Prescribed and Administered Therapy for this visit/hospitalization:
(Reported by most recent date first)
9/7/2022
7/26/2022--Wellness Plan Monthly Payment-- - Completed
Office Visit - Completed
Blood Sample Collect / Prep - Completed
Complete Blood Cell Count (CBC/5 part machine
differential) - Completed
Day Care for Optimum Exam - Completed
Ophthalmic Exam - Complete - Completed
Rectal Exam - Brief - Completed
Fecal Sample Collect / Prep - Completed
Intestinal Parasite Fecal Exam - Completed
Diphenhydramine Injection (Pre-Vaccination) - Completed
Pyrantel Pamoate 50mg/ml (per ml) - Completed
Urinalysis Test (Individual) - Completed
Urine Sediment Exam - Completed
Ear Cleaning Level 1 - Completed
Ear Swab with Cytology & Stain - Completed
Oticetic Ear Flush 4oz - Completed
8/26/2022--Wellness Plan Monthly Payment-- -
Completed
Physical Exam: First Pet - Completed
Canine Heartworm/Lyme/Ehrlichia/Anaplasma SNAP
Test - Completed
Comprehensive Exam - Canine - Completed
Exam - Dental - Completed
Otoscopic Exam - Complete - Completed
Express Anal Glands - Completed
Internal Organ Function Screen - Completed
Pre-Vaccination Package, High Risk Breed - Completed
ProHeart 6 (<25lbs) Injection - Completed
Medical Waste Disposal Fee - Completed
Urine Sample Collect/Prep - Completed
Urine Specific Gravity - Completed
Ear Hair Removal - Completed
Mometamax Otic Solution (15gm) - Completed
Time Printed: 1:18 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 7 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Wednesday, September 7, 2022 9:07 AM
Care Provided at
Laurel MD on
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
9/7/2022 4:16 PM
Plan Jones, S. Wooten, K. Entzminger, E. 1364 Laurel
ProHeart Administration
Administered at: 09/07/2022 9:42 AM
Lot Number: 517012
Amount Given: 0.67 ml
Site of Administration: Left Front Leg
Route: Subcutaneous Injection
9/7/2022 3:38 PM
Plan Jones, S. Wooten, K. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 9/7/2022 Prescription #: 1364-12914396
Rx: Oticetic Ear Flush 4oz Manufacturer:
Instructions: Instill as directed by your veterinarian
Place a small amount of cleanser into both ears every 12 hours for 7 consecutive
days. Massage base of the ear canal to break up wax. Remove excess cleanser &
wax with cotton gauze. Use TWICE weekly AFTER to keep ears clean / healthy.
For use in both ears.
Shake well before use.
Store at room temperature.
Providing Doctor: Susan J Jones Quantity: 1.00
Discard By: 3/8/2023 Number of Refills: 1 Refill Expiration Date: 3/7/2023
9/7/2022 3:38 PM
Plan Jones, S. Wooten, K. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 9/7/2022 Prescription #: 1364-12914397
Rx: Mometamax Otic Solution (15gm) Manufacturer:
Instructions: Instill 6 drops every 24 hours for 7 days
CLEAN EARS BEFORE EACH USE. Place 6 drops in both ears every 24 hours for 7
consecutive days. Massage base of the ear canal to distribute medication down in
ear canal. Discontinue and recheck if ears worsen or deafness occurs with use.
Shake well before use.
Store at room temperature.
Monitor for signs of head tilt, incoordination, circling.
Providing Doctor: Susan J Jones Quantity: 1.00
Discard By: 3/8/2023 Number of Refills: 0 Refill Expiration Date: 3/7/2023
9/7/2022 9:44 AM
Plan Jones, S. Wooten, K. Entzminger, E. 1364 Laurel
Updated microchip information for Chewy Bear:
Original Microchip ID: Original Manufacturer:
New Microchip ID: 985112007160438 New Manufacturer: Home Again
9/7/2022 9:42 AM
Time Printed: 1:18 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 8 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Wednesday, September 7, 2022 9:07 AM
Care Provided at
Laurel MD on
Plan Jones, S. Wooten, K. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 9/7/2022 Prescription #: 1364-12914370
Rx: Pyrantel Pamoate 50mg/ml (per ml) Manufacturer: Apexa
Instructions: Give 3 mls one time
Providing Doctor: Susan J Jones Quantity: 3.00
Discard By: 3/8/2023 Number of Refills: N/A Refill Expiration Date: N/A
9/7/2022 9:42 AM
Plan Jones, S. Wooten, K. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 9/7/2022 Prescription #: 1364-12914323
Rx: Diphenhydramine Injection (Pre-Vaccination) Manufacturer:
Instructions: Inject 0.58 mls one time
Providing Doctor: Susan J Jones Quantity: 0.58
Discard By: 3/8/2023 Number of Refills: N/A Refill Expiration Date: N/A
9/7/2022 9:07 AM
Assessment Jones, S. Wooten, K. Entzminger, E. 1364 Laurel
dx: patellar luxation, overweight, full but normal AGs, otitis externa (suspected)
9/7/2022 9:07 AM
Objective Jones, S. Wooten, K. Entzminger, E. 1364 Laurel
TPR within normal limits. BAR. wt: 29.06# /13.18 kg
NT: mm pink, moist, CRT < 2 sec. Very mild dental calculus and gingivitis
Eyes: OU - fundic exam NSF
Ears: AU - mild to mod fur, mild light brown exudate intermixed in fur
H/L: auscult WNL
Abd: relaxed, NSF
MS: Gr 1/4 medial patellar luxation bilateral, L luxates more readily than R
Rectal: full, easily expressed AGs
BCS: 6/9
Rest of PE NSF
9/7/2022 9:07 AM
Plan(Notes) Jones, S. 1364 Laurel
Time Printed: 1:18 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 9 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Wednesday, September 7, 2022 9:07 AM
Care Provided at
Laurel MD on
comp exam
fecal: see labs
4 Dx: neg
CBC/Chem: minor changes, overall NSF
UA: SpG 1.055, trace protein (r/o spurious d/t high SpG), pH 6.0 sediment inactive
ear swab: AS - scattered yeast, AD: NSF (will have client treat both since both ears have same
appearance)
AG expression
ear hair removal, ear cleaning level
pyrantel (50 mg/mL) 3.0 mL PO in hosp
diphenhydramine inj (50 mg/ml) 0.60 mL IM RR leg prior to vax
Proheart 6 Inj (0.0227 ml/lb) 0.67 mL SQ
Dispensed: otic cleanser and medication
1. Prognosis: Fair without to Good with current recommendations, treatment, and owner
compliance
2. Client Education: flea/tick and HW prevention, vaccine schedule, vaccine reactions
3. Recheck: 1 wk
4. Follow up therapy: recheck ears
***********************************************************************
9/7/2022 9:07 AM
Subjective Jones, S. Wooten, K. Entzminger, E. 1364 Laurel
Presented for a comrpehensive exam and OWP services. No health concerns indicated at this time.
Home Care Instructions documented for this visit/hospitalization:
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
None
Therapy presented & declined by the client for this visit/ hospitalization:
None
Therapy considered but not medically necessary for this visit/hospitalization:
Pedicure - Not Medically Necessary Pyrantel Pamoate 50mg/ml (per ml) - Not Medically
Necessary
Therapy postponed by the client or doctor this visit/hospitalization:
None
Time Printed: 1:18 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 10 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Wednesday, September 7, 2022 9:07 AM
Care Provided at
Laurel MD on
Chewy Bear was presented on 2/22/2022 for: Preventive Care-Vaccination/Deworming,
schedule dental after this appt
Subjective
See 'Plan and Other Notes' section for patient history documentation, if pertinent.
Visit Info: Chewy Bear's visit began at 9:08 AM on 2/22/2022 and ended on 2/22/2022
Doctors Assisting or Consulting with Care:
Medical Authorization Release Signed?
Future appointment(s) scheduled for:
None agreed to by client
Dr. Jamila Y Echols, Dr. Sabrina Owens
Yes
Patient Information on 2/22/2022
Name: Chewy Bear
Species: Canine
Breed: Terrier, Yorkshire
Gender: Male (Neutered)
Description: brn
Date of Birth: 9/30/2015
Optimum Wellness Plan: Active Care Plus
Microchip #: 985112007160438 Home Again
Chewy Bear has visited this Banfield Hospital 6 times.
Chewy Bear's first visit on 3/15/2021 at this hospital
Chewy Bear's last visit on 2/22/2022 at this hospital
Weight: 28.60 Lbs/12.97 Kgs
Preventive Care Given Due Date Preventive Care Given Due Date
Heartworm Prevention 8/31/2021 3/1/2022 Heartworm Test 8/31/2021 8/31/2022
Flea Prevention 10/19/2021 4/17/2022 Lyme Test 8/31/2021 8/31/2022
Tick Prevention 10/19/2021 4/17/2022 Ehrlichia test 8/31/2021 8/31/2022
Roundworms 2/22/2022 8/21/2022 Anaplasma Test 8/31/2021 8/31/2022
Hookworms 2/22/2022 8/21/2022 Blood Cell Count 2/22/2022 8/21/2022
Rabies 9/2/2020 9/2/2023 Serum Chemistries 2/22/2022 8/21/2022
DAPP 6/21/2021 6/21/2024 Differential Exam 2/22/2022 8/21/2022
Leptospirosis 2/22/2022 2/22/2023 Electrolytes 2/22/2022 2/22/2023
Bordetella 2/22/2022 2/22/2023 Fecal Exam 2/22/2022 8/21/2022
Lyme 2/22/2022 2/22/2023 Urine Specific Gravity 8/31/2021 8/31/2022
Dental Prophylaxis 2/22/2022 2/22/2023 Urine Strip Tests 8/31/2021 8/31/2022
Diphenhydramine 2/22/2022 2/23/2022 Urine Sediment Exam 8/31/2021 8/31/2022
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 1 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, February 22, 2022 9:08 AM
Care Provided at
Laurel MD on
Abnormal Findings:
Overall Condition Body Condition Score - Above Ideal
Otic Aberrant Hair - Left Ear Aberrant Hair - Right Ear
Oral/Nasal Tartar on Teeth - Found Swelling/Inflammation of Gums - Found
Normal or Not Selected Findings:
Overall Condition Nutritional Evaluation Complete Overall Evaluation Complete
Coat and Skin Coat/Skin Normal
Ocular Ocular Normal
Respiratory Respiratory Normal
Cardiovascular Cardiovascular Normal
Abdominal Abdominal Normal
Urogenital Urogenital Normal
Perineal Perineal Normal
Musculoskeletal Musculoskeletal Normal
Neurological Neurological Normal
Laboratory Results: (é = above normal; ê = below normal; ********** = could not be evaluated)
Temperature: 101.2º F -
Heart Rate: 124/min -
Respiration: 32/min -
Capillary Refill Time: Under 2 Seconds
Exam was certified by Dr. Jamila Y Echols, DVM on 2/22/2022
Physical Exam Findings on 2/22/2022
Objective
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 2 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, February 22, 2022 9:08 AM
Care Provided at
Laurel MD on
Recorded on 2/22/2022 4:48:05 PM
Test Name Result Units Range
Albumin (ALB) 3.9 g/dL (2.300-4.000)
Alkaline Phosphatase (ALKP) ê <10.0 U/L (23.000-212.000)
ALT/SGPT (ALT) 97.0 U/L (10.000-125.000)
BUN (Blood Urea Nitrogen) 14.0 mg/dL (7.000-27.000)
Calcium (CA) 9.9 mg/dL (7.900-12.000)
Cholesterol (CHOL) 276.0 mg/dL (110.000-320.000)
Creatinine (CREA) 0.9 mg/dL (0.500-1.800)
Gamma Glutamyl Transferase (GGT) 0.0 U/L (0.000-11.000)
Globulin (GLOB) 4.0 g/dL (2.500-4.500)
Glucose (GLU) 102.0 mg/dL (74.000-143.000)
Phosphorus (PHOS) 5.3 mg/dL (2.500-6.800)
Bilirubin, Total (TBIL) é 1.0 mg/dL (0.000-0.900)
Protein, Total (TP) 7.9 g/dL (5.200-8.200)
ALB/Glob 1.0
BUN/Crea 16.0
Recorded on 2/22/2022 4:48:10 PM
Test Name Result Units Range
Sodium (Na+) 155.0 mmol/L (144.000-160.000)
Potassium (K+) 3.7 mmol/L (3.500-5.800)
Chloride (CL-) 113.0 mmol/L (109.000-122.000)
Na+/K+ 42.0
Osmolality 305.0 mmol/kg
Recorded on 2/22/2022 4:52:02 PM
Test Name Result Units Range
Fecal - Roundworm Eggs NEGATIVE
Fecal - Hookworm Eggs NEGATIVE
Fecal - Whipworm Eggs NEGATIVE
Fecal - Giardia NEGATIVE
Fecal - Coccidia Oocysts NEGATIVE
Fecal - Tapeworms NEGATIVE
Fecal - Abnormal Bacteria NEGATIVE
Fecal - Significant Blood NEGATIVE
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 3 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, February 22, 2022 9:08 AM
Care Provided at
Laurel MD on
Fecal - 'Other' Eggs NEGATIVE
Recorded on 2/22/2022 5:37:16 PM
Test Name Result Units Range
Electrocardiogram Interpretation NORMAL
Hospital Comments: nsr
Recorded on 2/22/2022 5:42:48 PM
Test Name Result Units Range
WBC 15.42 10^9/l (6.000-17.000)
Lymphocyte 3.6 10^9/l (1.000-4.800)
Monocyte 1.33 10^9/l (0.200-1.500)
Neutrophil 10.37 10^9/l (3.000-12.000)
Eosinophil 0.1 10^9/l (0.000-0.800)
Basophil 0.01 10^9/l (0.000-0.400)
Lymphocyte, % 23.4 % (9.000-47.000)
Monocyte, % 8.7 % (2.000-12.000)
Neutrophil, % 67.3 % (42.000-84.000)
Eosinophil, % ê 0.7 % (1.000-18.000)
Basophil, % 0.1 % (0.000-1.100)
RBC Count (RBC) 7.72 10^12/l (5.500-8.500)
Hemoglobin (HGB) é 18.3 g/dl (12.000-18.000)
Hematocrit (HCT) 52.04 % (37.000-55.000)
MCV 67.0 fl (60.000-77.000)
MCH 23.7 pg (19.500-24.500)
MCHC 35.2 g/dl (31.000-39.000)
RDW 16.2 % (14.000-20.000)
Platelet Count (PLT) ê 88.0 10^9/l (165.000-500.000)
PCT ê 0.09 % (0.150-0.390)
MPV 9.9 fl (3.900-11.100)
Assessment
Tentative Diagnosis Status Date Hospital Team Member
Dental Calculus Condition Resolved 2/22/2022 1364 Laurel
Epiphora Stable/Persistent/Chronic 2/22/2022 1364 Laurel
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 4 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, February 22, 2022 9:08 AM
Care Provided at
Laurel MD on
Periodontal Disease Stage 2 Stable/Persistent/Chronic 2/22/2022 1364 Laurel
Patella Luxation, Medial, Grade 1 Stable/Persistent/Chronic 3/20/2021 1364 Laurel
Otitis Externa, Medical Undergoing Therapy 9/2/2020 1182 Largo
Dental Calculus Undergoing Therapy 12/14/2019 1182 Largo
Anal Sacs, Full (Otherwise Normal) Needs Protocol 3/9/2019 1182 Largo
Patellar Luxation, Medical Stable/Persistent/Chronic 3/9/2019 1182 Largo
Cystitis Undergoing Therapy 6/11/2018 1006
Calverton
Otitis Externa, Medical Undergoing Therapy 3/3/2018 1006
Calverton
Constipation, Conservative Needs Protocol 11/18/2017 1006
Calverton
Granuloma, Acral Lick Stable/Persistent/Chronic 7/6/2017 1182 Largo
Epiphora Stable/Persistent/Chronic 6/14/2017 1182 Largo
Patellar Luxation, Medical Needs Protocol 6/14/2017 1182 Largo
Pruritus Undergoing Therapy 6/14/2017 1182 Largo
Dental Calculus Undergoing Therapy 6/8/2017 1006
Calverton
Healthy Pet Needs Protocol 5/31/2017 1182 Largo
Plan and Other Notes
Prescribed and Administered Therapy for this visit/hospitalization:
(Reported by most recent date first)
2/22/2022
Office Visit - Completed
Comprehensive Exam - Canine - Completed
Exam - Dental - Completed
Otoscopic Exam - Complete - Completed
Dental Prophylaxis Canine Package - Completed
Antisedan (Atipamazole) 5mg/ml Injectable (per ml) -
Completed
Blood Sample Collect / Prep - Completed
Complete Blood Cell Count (CBC/5 part machine
differential) - Completed
Dexmedetomidine 0.5mg/ml Injectable (per ml) -
Completed
Electrolytes (K, Na, Cl, Na/K) - Completed
Hospitalization-Doctor's Supervision - Completed
Physical Exam: Wellness Plan - Completed
Day Care for Optimum Exam - Completed
Ophthalmic Exam - Complete - Completed
Rectal Exam - Brief - Completed
Anesthesia Canine Dental - Completed
Blood Pressure Monitoring, Anesthesia - Completed
Butorphanol 10mg/ml Injectable (per ml) - Completed
Dental Prophylaxis - Completed
Electrocardiogram Monitoring - Completed
Fluid Administration - Lactated Ringers Solution -
Completed
Hospitalization-Hospital Team Care - Completed
Internal Organ Function Screen - Completed
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 5 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, February 22, 2022 9:08 AM
Care Provided at
Laurel MD on
Additional Medical Notes documented for this visit/hospitalization:
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
2/22/2022 5:42 PM
Plan Echols, J. Rey, A. Entzminger, E. 1364 Laurel
The Lab Results for Complete Blood Cell Count (CBC/5 part machine differential) were manually
entered.
2/22/2022 4:49 PM
Plan Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Administered at: 02/22/2022 4:14 PM
Preventive Care: Vaccine - Canine Lyme Route: Subcutaneous Site: Left Front Leg
Producer: Zoetis Expiration Date: 2/22/2023
Lot Number: 526385 Lot Expiration:8/16/2023
Combination/Product Given: Lyme Alone (Vanguard crLyme)
2/22/2022 4:49 PM
Plan Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Administered at: 02/22/2022 4:14 PM
Preventive Care: Vaccine - Canine Bordetella Route: Subcutaneous Site: Left Rear
Producer: Merck Expiration Date: 2/22/2023
Lot Number: 507227 Lot Expiration:4/10/2024
Combination/Product Given: Bordetella Alone (Bronchicine Injectable)
2/22/2022 4:49 PM
Plan Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Hospitalization-Ward Fee - Completed
IV Catheter Insertion - Completed
IV Fluid Administration Set (Each) - Completed
Pre-Anesthetic Examination - Completed
Propofol Injectable (per ml) - Completed
Recovery Care After Anesthesia - Completed
Ear Hair Removal - Completed
Fecal Sample Collect / Prep - Completed
Pedicure - Completed
Medical Waste Disposal Fee - Completed
Diphenhydramine Injection (Pre-Vaccination) - Completed
Vaccine - Canine Leptospirosis 4-way - Completed
IV Extension Set (Each) - Completed
IV Fluids Pump - Completed
Pre-Med/Induction Injectable - Completed
Pulse Oximeter - Completed
Tracheal Intubation - Completed
Express Anal Glands - Completed
Intestinal Parasite Fecal Exam - Completed
Pyrantel Pamoate 50mg/ml (per ml) - Completed
Pre-Vaccination Package, High Risk Breed - Completed
Vaccine - Canine Bordetella - Completed
Vaccine - Canine Lyme - Completed
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 6 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, February 22, 2022 9:08 AM
Care Provided at
Laurel MD on
Administered at: 02/22/2022 4:14 PM
Preventive Care: Vaccine - Canine Leptospirosis 4-way Route: Subcutaneous Site: Right Front Leg
Producer: Merck Expiration Date: 2/22/2023
Lot Number: 02171264 Lot Expiration:11/16/2023
Combination/Product Given: Lepto Alone (Nobivac L4 )
2/22/2022 4:14 PM
Plan Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 2/22/2022 Prescription #: 1364-12753195
Rx: Diphenhydramine Injection (Pre-Vaccination) Manufacturer:
Instructions: Inject 0.57 mls one time
Providing Doctor: Jamila Echols Quantity: 0.57
Discard By: 8/23/2022 Number of Refills: N/A Refill Expiration Date: N/A
2/22/2022 2:19 PM
Plan Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Called client and lvm to let client know that both pets did well for their dental cleaning and will be
ready to picked up around 4:30pm. -AR
2/22/2022 2:00 PM
Plan Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 2/22/2022 Prescription #: 1364-12753194
Rx: Pyrantel Pamoate 50mg/ml (per ml) Manufacturer: Apexa
Instructions: Give 2.9 mls one time
Start tomorrow.
Give by mouth only.
Providing Doctor: Jamila Echols Quantity: 2.90
Discard By: 8/23/2022 Number of Refills: 0 Refill Expiration Date: 8/22/2022
2/22/2022 2:00 PM
Plan Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 2/22/2022 Prescription #: 1364-12753200
Rx: Propofol Injectable (per ml) Manufacturer: Abbott
Instructions: Inject 10 mls one time
Providing Doctor: Jamila Echols Quantity: 10.00
Discard By: 8/23/2022 Number of Refills: N/A Refill Expiration Date: N/A
2/22/2022 2:00 PM
Plan Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 2/22/2022 Prescription #: 1364-12753196
Rx: Fluid Administration - Lactated Ringers Solution Manufacturer:
Instructions: Administer 10.3 mls one time
Providing Doctor: Jamila Echols Quantity: 10.30
Discard By: 8/23/2022 Number of Refills: N/A Refill Expiration Date: N/A
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 7 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, February 22, 2022 9:08 AM
Care Provided at
Laurel MD on
2/22/2022 2:00 PM
Plan Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 2/22/2022 Prescription #: 1364-12753201
Rx: Dexmedetomidine 0.5mg/ml Injectable (per ml) Manufacturer:
Instructions: Inject 0.13 mls one time
Providing Doctor: Jamila Echols Quantity: 0.13
Discard By: 8/23/2022 Number of Refills: N/A Refill Expiration Date: N/A
2/22/2022 2:00 PM
Plan Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 2/22/2022 Prescription #: 1364-12753199
Rx: Butorphanol 10mg/ml Injectable (per ml) Manufacturer:
Instructions: Inject 0.52 mls one time
Providing Doctor: Jamila Echols Quantity: 0.52
Discard By: 8/23/2022 Number of Refills: N/A Refill Expiration Date: N/A
2/22/2022 2:00 PM
Plan Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Patient: Chewy Bear (Canine) Client: Nelly Diaz
Prescription Filled On: 2/22/2022 Prescription #: 1364-12753202
Rx: Antisedan (Atipamazole) 5mg/ml Injectable (per ml) Manufacturer:
Instructions: Inject 0.13 mls one time
Providing Doctor: Jamila Echols Quantity: 0.13
Discard By: 8/23/2022 Number of Refills: N/A Refill Expiration Date: N/A
2/22/2022 9:09 AM
Assessment Entzminger, E. 1364 Laurel
Epiphora Stable/Persistent/Chronic
Periodontal Disease Stage 2 Stable/Persistent/Chronic
Dental Calculus Condition Resolved
2/22/2022 9:09 AM
Objective Entzminger, E. 1364 Laurel
2/22/2022 9:09 AM
Plan(Notes) Echols, J. Rey, A. Entzminger, E. 1364 Laurel
Routine dentistry:
__Chewy Bear____has:
Generalized moderate plaque.
Generalized moderate calculus.
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 8 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, February 22, 2022 9:08 AM
Care Provided at
Laurel MD on
Generalized mild gingivitis.
Recommendations:Daily brushing, CET chews, or Greenies
Complete dental prophylaxis: yes
Home dental care:
----------------------------------------------------
Examination Notes.
S: Pet presented for dental cleaning. O noted
O: BARH, MM pink/moist, CRT <2 sec, dental calculus/gingivitis, EENT: epiphora AU, ears - aberrant
hair AU, abd pal:wnl, heart and lung sounds:wnl, ms:wnl, skin:wnl
A: Epiphora Stable/Persistent/Chronic
Periodontal Disease Stage 2 Stable/Persistent/Chronic
Dental Calculus Condition Resolved
P: Exam
CBC/Chemistry/Electrolytes: wnl
IV catheter/fluids (LRS) @ _40__ml/hr throughout procedure. Total: 10.3mls
Dental Prophy
2 hours after recovery:
diphenhydramine inj (50 mg/ml) 0.57 ml IM prior to vax
Lepto 1 yr
Lyme 1 yr
Bord IN 1 yr
Premed: Butorphanol (10mg/ml) 0.52mL /dexmedetomidine (0.5mg/ml) 0.13mL IM at _1:20___. P
returned to kennel.
Induction: Inserted size _22g_ catheter into _RF_ leg. Administered __7_ml Propofol (10mg/ml).
Discarded 3mls of Propofol.
Maintenance: Inserted size 6.5_ Endotracheal tube. Sevofluorane gas.
Sx:Monitored pet with ECG, and Pulse OX. Administered fluids of LRS at_40__ml/hr. Routine dental
prophy performed. Returned to kennel, extubated, and monitored until discharge without
complications. Removed catheter at time of discharge.
1 Prognosis: Good
2 Client Education: Exam findings. Test results. Recommend monthly F/T/HW prevention. Monitor P
closely this evening since she was under anesthesia today. Offer food this evening or early tomorrow
morning. P may be lethargic up to 48 hours after the anesthetic procedure. P may have mild nausea
and/or mild loose stools after the anesthetic procedure.
3 Recheck: 2 weeks
4 Follow-Up Therapy: proheart inj
Team Member: AR/BS/Dr. E
-----------------------------------------------------------------------------
Anesthesia Machine Checklist performed by AR; Confirmed by Dr. Echols
ANESTHESIA
Cuff Appropriately Inflated and Pressure Checked: __x_ Yes ___ No
Pre-Induction T: 101.5 P: 112 R: 24
MAINTENANCE / MONITORING -
Time: 1:35 1:40 1:45
__x__ Sevo % -> 2 2 2
__x__ Oxygen Flow (L/min) -> 2.5 2.5 2.5
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 9 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, February 22, 2022 9:08 AM
Care Provided at
Laurel MD on
__x_ Heart Rate -> 110 108 106
__x__ Pulse Ox O2 -> 93 94 93
__x__ Respiratory Rate -> 25 11 10
__x__ CRT/memb. Color -> <2/pk <2/pk <2/pk
__x__ Pulse Quality -> str str str
__x__ ECG rhythm -> nsr nsr nsr
__x__ BP-> 107/81/90 114/68/83 122/80/94
__x__ Temperature-> 101.6 101.9 101.4
EQUIPMENT
Vaporizer Type: Vasco Anesthesia Machine Type: Vasco
Breathing Circuit: ____ Nonrebreathing __x__ Rebreathing
System Leak Test Performed: __x__Yes ____ No
Absorber Type: Sodalime
***********************************************************************
2/22/2022 9:09 AM
Subjective Echols, J. Entzminger, E. 1364 Laurel
O concerned bout weight. O says P eats the hills diet we prescribed for dry food and hills non
prescription weight management wet food. says she feels like he is still gaining.
Home Care Instructions documented for this visit/hospitalization:
(Reported by most recent date first)
Date Type Note Doctor VT/VA CSC Hospital
None
Therapy presented & declined by the client for this visit/ hospitalization:
Cerenia 10mg/ml Injectable (per ml) - Client Declines
Internal Organ Function Screen - Client Declines
Electrolytes (K, Na, Cl, Na/K) - Client Declines
Superchem / CBC - Client Declines
Complete Blood Cell Count (CBC/5 part machine differential) -
Client Declines
Blood Sample Collect / Prep - Client Declines
Therapy considered but not medically necessary for this visit/hospitalization:
Ear Cleaning Level 1 - Not Medically Necessary
Electrolytes (K, Na, Cl, Na/K) - Not Medically Necessary
Complete Blood Cell Count (CBC/5 part machine
differential) - Not Medically Necessary
Therapy postponed by the client or doctor this visit/hospitalization:
Internal Organ Function Screen - Postponed
Time Printed: 1:17 PM Date Printed: 8/14/2023
Report ID: MedSummary.en.x Hospital #1364 Page 10 of 10
13600 Baltimore Ave, Suite 160
Laurel, MD 20707-0707
(301) 604-1414
Banfield Pet Hospital
Nelly Diaz
6711 Dorman St
Hyattsville, MD 207842515
Cell Phone: (301) 437-9425
ndiazrod09@gmail.com
Medical Summary Report
Tuesday, February 22, 2022 9:08 AM
Care Provided at
Laurel MD on"""
    }
    DocumentTypeClassificationForInsuranceOcrDataCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'ocr_text': 'sample_value'
    }
    try:
        DocumentTypeClassificationForInsuranceOcrDataCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        DocumentTypeClassificationForInsuranceOcrDataCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'ocr_text': 'sample_value'
    }
    try:
        DocumentTypeClassificationForInsuranceOcrDataCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
