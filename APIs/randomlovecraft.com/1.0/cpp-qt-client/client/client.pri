QT += network

HEADERS += \
# Models
    $${PWD}/OAIBook.h \
    $${PWD}/OAIGet_books_200_response.h \
    $${PWD}/OAIGet_sentences_from_book_200_response.h \
    $${PWD}/OAIGet_specific_sentence_200_response.h \
    $${PWD}/OAISentence.h \
# APIs
    $${PWD}/OAIBooksApi.h \
    $${PWD}/OAISentencesApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIBook.cpp \
    $${PWD}/OAIGet_books_200_response.cpp \
    $${PWD}/OAIGet_sentences_from_book_200_response.cpp \
    $${PWD}/OAIGet_specific_sentence_200_response.cpp \
    $${PWD}/OAISentence.cpp \
# APIs
    $${PWD}/OAIBooksApi.cpp \
    $${PWD}/OAISentencesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
