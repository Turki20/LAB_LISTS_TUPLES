movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


def calculateAverage(_list):
    '''
     Calculates the average rating for each movie.
     
     Args:
        list of movies
        
     Return:
        new list with average
    '''
    new_list = []
    for movie in _list:
        sum = 0
        for rate in movie[2]:
            sum += rate
        avg = sum / len(movie[2])
        new_tuple = movie + (round(avg, 2),)
        new_list.append(new_tuple)
        
    return new_list


new_list_with_avg = calculateAverage(movies)
new_list_with_avg.sort(key=lambda m: m[3], reverse=True) # sort the list based on average

index = 0 
for i in new_list_with_avg:
    if i[3] < 6:
        break
    index += 1
    
final_list = new_list_with_avg[:index] # remove a movies that less than 6 avg

for i in range(0, len(final_list)): # print all movies
    print(f"{i + 1}. {final_list[i][0]} ({final_list[i][1]}) - Average rating: {final_list[i][3]} ◆")