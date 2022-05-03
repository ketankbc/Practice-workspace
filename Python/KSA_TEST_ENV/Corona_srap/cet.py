import tabula


#df = ("/Users/ketan/Documents/Practice-workspace/Python/KSA_TEST_ENV/Corona_srap/CET ranking.pdf")
#output = "/Users/ketan/Documents/Practice-workspace/Python/KSA_TEST_ENV/Corona_srap/CET_test.csv"
#tabula.convert_into(df, output, output_format="csv", stream=True)


#import tabula

df = tabula.read_pdf("/Users/ketan/Documents/Practice-workspace/Python/KSA_TEST_ENV/Corona_srap/CET ranking.pdf", pages='all')
tabula.convert_into("/Users/ketan/Documents/Practice-workspace/Python/KSA_TEST_ENV/Corona_srap/CET_test.csv", output_format="csv",pages='all', stream=True)