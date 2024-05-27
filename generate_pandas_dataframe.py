# this file generates a states.csv file with states and their locations in it extracted from
# the given gif image
import pandas

data = pandas.DataFrame

# these locations have already been read by the clicking through the mouse and made it as a dictionary
# to be imported by the pandas library, you can add more states by this method using the read_from_gif file
dic = {
    'state': ['jammu and kashmir',
              'himachal',
              'punjab',
              'uttarakhand',
              'haryana',
              'delhi',
              'rajasthan',
              'madhya pradesh',
              'uttar pradesh'],

    'location': [(-140.0, 291.0),
                 (-119.0, 220.0),
                 (-161.0, 191.0),
                 (-75.0, 173.0),
                 (-143.0, 150.0),
                 (-120.0, 134.0),
                 (-191.0, 80.0),
                 (-102.0, 1.0),
                 (-47.0, 86.0)]
}
data = pandas.DataFrame(dic)

data.to_csv('states.csv')
