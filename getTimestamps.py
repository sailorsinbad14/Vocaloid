def getTimestamps(response):
    timestamps = '\nTimestamps: <br>'

    for result in response.results:
        alternative = result.alternatives[0]
        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
            timestamps +='\n' + '{} , {}'.format(
                start_time.seconds + start_time.nanos * 1e-9,
                word

                ) + '<br>'
    return timestamps

 # timestamps +='\n' + 'Word: {}  < {} - {}'.format(
 #                word,
 #                start_time.seconds + start_time.nanos * 1e-9,
 #                end_time.seconds + end_time.nanos * 1e-9 ) + '><br>'