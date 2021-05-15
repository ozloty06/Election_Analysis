# Election_Analysis

## Project Overview
Seth and Tom are Colorado Board of Elections employees and have asked for help pulling together an election audit analysis of a recent local election to be submitted to the election commission. They have requested the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of the candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.5, Visual Studio Code, 

An analysis of election data in a CSV file using Python in VS Code, 1.56.1

## Election-Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The county results include:
  - Jefferson county had 10.5% of votes and a total count of 38,855 votes.
  - Denver county had 82.8% of votes and a total count of 306,055 votes.
  - Arapahoe county had 6.7% of votes and a total count of 24,801 votes.
- The county with the most votes was:
  - Denver, which had 82.8% of the votes and a total vote count of 306,055 votes.
- The candidates were:
  - Candidate 1: Charles Casper Stockham
  - Candidate 2: Diana DeGette
  - Candidate 3: Raymon Anthony Doane
- The candidate results were:
  - Candidate 1, Charles Casper Stockham, received 23% of the vote and 85,213 number of votes.
  - Candidate 2, Diana DeGette, received 73.8% of the vote and 272,892 number of votes.
  - Candidate 3, Raymon Anthony Doane, received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Candidate 2, Diane DeGette, who received 73.8% of the votes and 272,892 nuymber of votes.

## Election-Audit Summary
As an added benefit to the election commission, this script was written in such a way that it can easily be repurposed for additional election audit opportunities. The script accepts election results in a simple text format known as a .csv file, or comma separated values. This allows for handling large data sets extending beyond the initial three counties and three candidates included in our analysis. Further, this script can be modified in several ways to provide additional analysis for the elections commission, including:
- Voter Party Affiliation. 
&nbsp;&nbsp;&nbsp;&nbsp;Voters can optionally provide their party affilation as they cast their votes which can be used to study both the distribution of the party within the county votes and for each of the candidates in the election. This would potentially require a modification to the ballot, adjustment to the .csv file to provide the raw data on party affiliation, and adjustments to logic loops included in the code for both county and candidate related analysis. Output would include a breakdown of party affilations within each county and for each candidate.
- Proposal Analysis.
&nbsp;&nbsp;&nbsp;&nbsp; While the current script analyzes candidate results, the program could be easily modified to evaluate quantity of voters for or against  proposed state or local ballot proposition(s). This analysis would still provide a breakdown by county as well as for each proposition. 
