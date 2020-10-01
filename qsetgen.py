import random

def proccess_subject(filename):
    """function to generate a dataframe from a subject questions excel data

    Args:
        filename (string): name of file containing the subject questions data
    """
    df=pd.read_excel(filename+".xlsx")



class bloomlevel():
    """Class for Bloom levels

    Returns:
        none: none
    """
    #stores no of entities in this bloom
    lenbloom=0 

    #function to initialize a bloom object
    def set_bloom(self,n,df):
        self.lenbloom=len(df[df["Blooms_level"]==n])
        self.data=df[df["Blooms_level"]==n]

    #function to return no of elements in this bloomlevel
    def len(self):
        return self.lenbloom

    #function to return all the other data of this bloomlevel(concatenated dataframe)
    def data(self):
        return self.data
    #flag will be used to determine no of questions to be fetched from this bloom level(defaults to 0)
    flag=0



def add_data(bloom,qset):
    """function to question data to the question set

    Args:
        bloom (bloomlevel): object of class bloomlevel
        qset (list): list of dictionaries containing question data

    Returns:
        list: returns a new list with added questions
    """
    temp=[]
    for i in range(bloom.len()):
        temp.append(i)
    flag=bloom.flag
    while(flag!=-1):
        for i in range(1):
            dat=bloom.data
            rand=random.choice(temp)
            qset.append(dict(dat.iloc[rand]))
            flag-=1
    return qset




def qset_gen(df):
    """function to generate unique question set from given dataframe

    Args:
        df (Dataframe): Dataframe containing the whole of questions data on the particular subject at hand

    Returns:
        list: returns list of dictionaries containing data for each question added to the unique question set
    """ 
    
    bloom1=bloomlevel()
    bloom1.set_bloom(1,df)
    bloom2=bloomlevel()
    bloom2.set_bloom(2,df)
    bloom3=bloomlevel()
    bloom3.set_bloom(3,df)
    
    
    if bloom1.len()>bloom2.len():
        bloom1.flag=1
        if bloom2.len()>bloom3.len():
            bloom2.flag=1
        else:
            bloom3.flag=1
    elif bloom3.len()>bloom1.len():
        bloom2.flag=1
        bloom3.flag=1
    else:
        bloom2.flag=1
        bloom1.flag=1
    
    qset=[]
    qset=add_data(bloom1,qset)
    qset=add_data(bloom2,qset)
    qset=add_data(bloom3,qset)
    
    return qset

def to_table(filename,qset):
    """function to convert unique question set to accessable excel format

    Args:
        filename (string): name you wish to give to question set
        qset (list of dicts): list of dicts containing selected questions data
    """
    dfn=pd.DataFrame(qset)
    dfn.to_excel(filename+".xlsx")

