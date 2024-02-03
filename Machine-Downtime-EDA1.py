# =============================================================================
# Machine - Downtime - EDA - 1
# =============================================================================
#Importing libraries
import pandas as pd                    #For data manipulation
import numpy as np                     #For numerical calculations - numerical python
import matplotlib.pyplot as plt        #For visualization
import seaborn as sns                  #Advanced data vizualization

#Reading the data
data = pd.read_csv(r"E:\360digiTMG-Project\Machine Downtime.csv")

data.head()
machine_eda = data.copy()

pd.set_option("display.max_columns",20)
pd.set_option("display.max_rows",5000)

machine_eda.info()

# Exploratory data analysis on raw data

# First moment business decision - measures of central tendency

# mean & median for contiuous variables

# Mean
machine_eda.Hydraulic_Pressure.mean()
machine_eda.Coolant_Pressure.mean()
machine_eda.Air_System_Pressure.mean()
machine_eda.Coolant_Temperature.mean()
machine_eda.Hydraulic_Oil_Temperature.mean()
machine_eda.Spindle_Bearing_Temperature.mean()
machine_eda.Spindle_Vibration.mean()
machine_eda.Tool_Vibration.mean()
machine_eda.Spindle_Speed.mean()
machine_eda.Voltage.mean()
machine_eda.Torque.mean()
machine_eda.Cutting.mean()

# Median
machine_eda.Hydraulic_Pressure.median()
machine_eda.Coolant_Pressure.median()
machine_eda.Air_System_Pressure.median()
machine_eda.Coolant_Temperature.median()
machine_eda.Hydraulic_Oil_Temperature.median()
machine_eda.Spindle_Bearing_Temperature.median()
machine_eda.Spindle_Vibration.median()
machine_eda.Tool_Vibration.median()
machine_eda.Spindle_Speed.median()
machine_eda.Voltage.median()
machine_eda.Torque.median()
machine_eda.Cutting.median()

# Mode
machine_eda.Date.mode()
machine_eda.Machine_ID.mode()
machine_eda.Assembly_Line_No.mode()
machine_eda.Downtime.mode()


# Second Moment Business Decision - Measures of Dispersion

# Variance
machine_eda.Hydraulic_Pressure.var()
machine_eda.Coolant_Pressure.var()
machine_eda.Air_System_Pressure.var()
machine_eda.Coolant_Temperature.var()
machine_eda.Hydraulic_Oil_Temperature.var()
machine_eda.Spindle_Bearing_Temperature.var()
machine_eda.Spindle_Vibration.var()
machine_eda.Tool_Vibration.var()
machine_eda.Spindle_Speed.var()
machine_eda.Voltage.var()
machine_eda.Torque.var()
machine_eda.Cutting.var()

# SD
machine_eda.Hydraulic_Pressure.std()
machine_eda.Coolant_Pressure.std()
machine_eda.Air_System_Pressure.std()
machine_eda.Coolant_Temperature.std()
machine_eda.Hydraulic_Oil_Temperature.std()
machine_eda.Spindle_Bearing_Temperature.std()
machine_eda.Spindle_Vibration.std()
machine_eda.Tool_Vibration.std()
machine_eda.Spindle_Speed.std()
machine_eda.Voltage.std()
machine_eda.Torque.std()
machine_eda.Cutting.std()

# Range
Hydraulic_Pressure_range = machine_eda.Hydraulic_Pressure.max() - machine_eda.Hydraulic_Pressure.min()
Coolant_Pressure_range = machine_eda.Coolant_Pressure.max() - machine_eda.Coolant_Pressure.min()
Air_System_Pressure_range = machine_eda.Air_System_Pressure.max() - machine_eda.Air_System_Pressure.min()
Coolant_Temperature_range = machine_eda.Coolant_Temperature.max() - machine_eda.Coolant_Temperature.min()
Hydraulic_Oil_Temperature_range = machine_eda.Hydraulic_Oil_Temperature.max() - machine_eda.Hydraulic_Oil_Temperature.min()
Spindle_Bearing_Temperature_range = machine_eda.Spindle_Bearing_Temperature.max() - machine_eda.Spindle_Bearing_Temperature.min()
Spindle_Vibration_range = machine_eda.Spindle_Vibration.max() - machine_eda.Spindle_Vibration.min()
Tool_Vibration_range = machine_eda.Tool_Vibration.max() - machine_eda.Tool_Vibration.min()
Spindle_Speed_range = machine_eda.Spindle_Speed.max() - machine_eda.Spindle_Speed.max()
Voltage_range = machine_eda.Voltage.max() - machine_eda.Voltage.min()
Torque_range = machine_eda.Torque.max() - machine_eda.Torque.min()
Cutting_range = machine_eda.Cutting.max() - machine_eda.Cutting.min()


# Third Moment Business Decision - Skewness
Hydraulic_Pressure_skew = machine_eda.Hydraulic_Pressure.skew()
Coolant_Pressure_skew = machine_eda.Coolant_Pressure.skew()
Air_System_Pressure_skew = machine_eda.Air_System_Pressure.skew()
Coolant_Temperature_skew = machine_eda.Coolant_Temperature.skew()
Hydraulic_Oil_Temperature_skew = machine_eda.Hydraulic_Oil_Temperature.skew()
Spindle_Bearing_Temperature_skew = machine_eda.Spindle_Bearing_Temperature.skew()
Spindle_Vibration_skew = machine_eda.Spindle_Vibration.skew()
Tool_Vibration_skew = machine_eda.Tool_Vibration.skew()
Spindle_Speed_skew = machine_eda.Spindle_Speed.skew()
Voltage_skew = machine_eda.Voltage.skew()
Torque_skew = machine_eda.Torque.skew()
Cutting_skew = machine_eda.Cutting.skew()

#Graphical Representation 

# Histogram
sns.distplot(machine_eda.Hydraulic_Pressure,kde=True)
sns.distplot(machine_eda.Coolant_Pressure,kde=True)
sns.distplot(machine_eda.Air_System_Pressure,kde=True)
sns.distplot(machine_eda.Coolant_Temperature,kde=True)
sns.distplot(machine_eda.Hydraulic_Oil_Temperature,kde=True)
sns.distplot(machine_eda.Spindle_Bearing_Temperature,kde=True)
sns.distplot(machine_eda.Spindle_Vibration,kde=True)
sns.distplot(machine_eda.Tool_Vibration,kde=True)
sns.distplot(machine_eda.Spindle_Speed,kde=True)
sns.distplot(machine_eda.Voltage,kde=True)
sns.distplot(machine_eda.Torque,kde=True)
sns.distplot(machine_eda.Cutting,kde=True)

# Bar plot
sns.countplot(y = machine_eda['Date'])
sns.countplot(y = machine_eda["Machine_ID"])
sns.countplot(y = machine_eda["Assembly_Line_No"])
sns.countplot(y = machine_eda['Downtime'])

# Scatterplot

sns.regplot(x = "Hydraulic_Pressure",y = "Hydraulic_Oil_Temperature",data = machine_eda)
sns.regplot(x = "Hydraulic_Pressure",y = 'Coolant_Pressure',data = machine_eda)
sns.regplot(x = 'Coolant_Temperature',y = 'Coolant_Pressure',data = machine_eda)
sns.regplot(x = 'Coolant_Temperature',y = 'Hydraulic_Oil_Temperature',data = machine_eda)

machine_eda.columns


# Correlation

# For categorical data
pd.crosstab(index = machine_eda.Machine_ID,columns = "count",dropna = True)
pd.crosstab(index = machine_eda.Assembly_Line_No,columns = "count",dropna = True)
pd.crosstab(index = machine_eda.Assembly_Line_No,columns = "count",dropna = True)
pd.crosstab(index = machine_eda.Downtime,columns = "count",dropna = True)


pd.crosstab(index = machine_eda.Machine_ID,columns = machine_eda['Assembly_Line_No'],dropna = True)
pd.crosstab(index = machine_eda.Machine_ID,columns = machine_eda['Downtime'],dropna = True)
pd.crosstab(index = machine_eda.Assembly_Line_No,columns = machine_eda['Downtime'],dropna = True)


pd.crosstab(index = machine_eda.Machine_ID,columns = machine_eda['Assembly_Line_No'],dropna = True,normalize=True)
pd.crosstab(index = machine_eda.Machine_ID,columns = machine_eda['Downtime'],dropna = True,normalize=True)
pd.crosstab(index = machine_eda.Assembly_Line_No,columns = machine_eda['Downtime'],dropna = True,normalize=True)
# From this we can check that we can remove "Assembly_Line_No variable , since machine_id and assembly_line_no are related

# For continuous data
numerical_variables = machine_eda.select_dtypes(exclude = [object])
corr_matrix = numerical_variables.corr()

sns.countplot(x = "Machine_ID",data = machine_eda,hue = "Downtime")




