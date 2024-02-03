
# =============================================================================
# Machine - Downtime - EDA - 1
# =============================================================================
#Importing libraries
import pandas as pd                    #For data manipulation
import numpy as np                     #For numerical calculations - numerical python
import matplotlib.pyplot as plt        #For visualization
import seaborn as sns                  #Advanced data vizualization


# Import processed file
data = pd.read_csv(r"E:\360digiTMG-Project\processed_file.csv",index_col=0)

processed_data = data.copy()

processed_data.columns

processed_data.head()

processed_data.info()


pd.set_option("display.max_columns",20)
pd.set_option("display.max_rows",3000)

# Exploratory data analysis on processed data

# First moment business decision - measures of central tendency

# mean & median for contiuous variables

# Mean
processed_data.Hydraulic_Pressure.mean()
processed_data.Coolant_Pressure.mean()
processed_data.Air_System_Pressure.mean()
processed_data.Coolant_Temperature.mean()
processed_data.Hydraulic_Oil_Temperature.mean()
processed_data.Spindle_Bearing_Temperature.mean()
processed_data.Spindle_Vibration.mean()
processed_data.Tool_Vibration.mean()
processed_data.Spindle_Speed.mean()
processed_data.Voltage.mean()
processed_data.Torque.mean()
processed_data.Cutting.mean()

# Median
processed_data.Hydraulic_Pressure.median()
processed_data.Coolant_Pressure.median()
processed_data.Air_System_Pressure.median()
processed_data.Coolant_Temperature.median()
processed_data.Hydraulic_Oil_Temperature.median()
processed_data.Spindle_Bearing_Temperature.median()
processed_data.Spindle_Vibration.median()
processed_data.Tool_Vibration.median()
processed_data.Spindle_Speed.median()
processed_data.Voltage.median()
processed_data.Torque.median()
processed_data.Cutting.median()

# Mode
processed_data.Date.mode()
processed_data.Machine_ID.mode()
processed_data.Downtime.mode()

# Variance
processed_data.Hydraulic_Pressure.var()
processed_data.Coolant_Pressure.var()
processed_data.Air_System_Pressure.var()
processed_data.Coolant_Temperature.var()
processed_data.Hydraulic_Oil_Temperature.var()
processed_data.Spindle_Bearing_Temperature.var()
processed_data.Spindle_Vibration.var()
processed_data.Tool_Vibration.var()
processed_data.Spindle_Speed.var()
processed_data.Voltage.var()
processed_data.Torque.var()
processed_data.Cutting.var()

# SD
processed_data.Hydraulic_Pressure.std()
processed_data.Coolant_Pressure.std()
processed_data.Air_System_Pressure.std()
processed_data.Coolant_Temperature.std()
processed_data.Hydraulic_Oil_Temperature.std()
processed_data.Spindle_Bearing_Temperature.std()
processed_data.Spindle_Vibration.std()
processed_data.Tool_Vibration.std()
processed_data.Spindle_Speed.std()
processed_data.Voltage.std()
processed_data.Torque.std()
processed_data.Cutting.std()

# Range
Hydraulic_Pressure_range1 = processed_data.Hydraulic_Pressure.max() - processed_data.Hydraulic_Pressure.min()
Coolant_Pressure_range1 = processed_data.Coolant_Pressure.max() - processed_data.Coolant_Pressure.min()
Air_System_Pressure_range1 = processed_data.Air_System_Pressure.max() - processed_data.Air_System_Pressure.min()
Coolant_Temperature_range1 = processed_data.Coolant_Temperature.max() - processed_data.Coolant_Temperature.min()
Hydraulic_Oil_Temperature_range1 = processed_data.Hydraulic_Oil_Temperature.max() - processed_data.Hydraulic_Oil_Temperature.min()
Spindle_Bearing_Temperature_range1 = processed_data.Spindle_Bearing_Temperature.max() - processed_data.Spindle_Bearing_Temperature.min()
Spindle_Vibration_range1 = processed_data.Spindle_Vibration.max() - processed_data.Spindle_Vibration.min()
Tool_Vibration_range1 = processed_data.Tool_Vibration.max() - processed_data.Tool_Vibration.min()
Spindle_Speed_range1 = processed_data.Spindle_Speed.max() - processed_data.Spindle_Speed.max()
Voltage_range1 = processed_data.Voltage.max() - processed_data.Voltage.min()
Torque_range1 = processed_data.Torque.max() - processed_data.Torque.min()
Cutting_range1 = processed_data.Cutting.max() - processed_data.Cutting.min()


# Third Moment Business Decision - Skewness
Hydraulic_Pressure_skew1 = processed_data.Hydraulic_Pressure.skew()
Coolant_Pressure_skew1 = processed_data.Coolant_Pressure.skew()
Air_System_Pressure_skew1 = processed_data.Air_System_Pressure.skew()
Coolant_Temperature_skew1 = processed_data.Coolant_Temperature.skew()
Hydraulic_Oil_Temperature_skew1 = processed_data.Hydraulic_Oil_Temperature.skew()
Spindle_Bearing_Temperature_skew1 = processed_data.Spindle_Bearing_Temperature.skew()
Spindle_Vibration_skew1 = processed_data.Spindle_Vibration.skew()
Tool_Vibration_skew1 = processed_data.Tool_Vibration.skew()
Spindle_Speed_skew1 = processed_data.Spindle_Speed.skew()
Voltage_skew1 = processed_data.Voltage.skew()
Torque_skew1 = processed_data.Torque.skew()
Cutting_skew1 = processed_data.Cutting.skew()




#Graphical Representation 

# Histogram
sns.distplot(processed_data.Hydraulic_Pressure,kde=True)
sns.distplot(processed_data.Coolant_Pressure,kde=True)
sns.distplot(processed_data.Air_System_Pressure,kde=True)
sns.distplot(processed_data.Coolant_Temperature,kde=True)
sns.distplot(processed_data.Hydraulic_Oil_Temperature,kde=True)
sns.distplot(processed_data.Spindle_Bearing_Temperature,kde=True)
sns.distplot(processed_data.Spindle_Vibration,kde=True)
sns.distplot(processed_data.Tool_Vibration,kde=True)
sns.distplot(processed_data.Spindle_Speed,kde=True)
sns.distplot(processed_data.Voltage,kde=False)
sns.distplot(processed_data.Torque,kde=False)
sns.distplot(processed_data.Cutting,kde=False)

# Bar plot
sns.countplot(y = processed_data["Machine_ID"])
sns.countplot(y = processed_data['Downtime'])

# Scatterplot

sns.regplot(x = "Hydraulic_Pressure",y = "Hydraulic_Oil_Temperature",data = processed_data)
sns.regplot(x = "Hydraulic_Pressure",y = 'Coolant_Pressure',data = processed_data)
sns.regplot(x = 'Coolant_Temperature',y = 'Coolant_Pressure',data = processed_data)
sns.regplot(x = 'Coolant_Temperature',y = 'Hydraulic_Oil_Temperature',data = processed_data)



# Correlation

# For categorical data
pd.crosstab(index = processed_data.Machine_ID,columns = "count",dropna = True)
pd.crosstab(index = processed_data.Downtime,columns = "count",dropna = True)


pd.crosstab(index = processed_data.Machine_ID,columns = processed_data['Downtime'],dropna = True)


pd.crosstab(index = processed_data.Machine_ID,columns = processed_data['Downtime'],dropna = True,normalize=True)
# From this we can check that we can remove "Assembly_Line_No variable , since machine_id and assembly_line_no are related

# For continuous data
numerical_variables = processed_data.select_dtypes(exclude = [object])
corr_matrix = numerical_variables.corr()

sns.countplot(x = "Machine_ID",data = processed_data,hue = "Downtime")

