def getTimestamps( response):
    same = dict()

    timestamps = '\nTimestamps:'
    # print (response.results)

    for result in response.results:
        alternative = result.alternatives[0]
        for word_info in alternative.words:
            word = word_info.word
            # print (word, word_info.start_time, word_info.end_time)
            start_time = word_info.start_time
            end_time = word_info.end_time
            same[start_time.seconds + start_time.nanos * 1e-9] = word
            timestamps +='\n' + '{} , {}'.format(
                start_time.seconds + start_time.nanos * 1e-9,
                word
                )

    return same, timestamps
 # timestamps +='\n' + 'Word: {}  < {} - {}'.format(
 #                word,
 #                start_time.seconds + start_time.nanos * 1e-9,
 #                end_time.seconds + end_time.nanos * 1e-9 ) + '><br>'
