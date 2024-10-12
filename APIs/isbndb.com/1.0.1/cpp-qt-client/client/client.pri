QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuthor.h \
    $${PWD}/OAIAuthorQueryResults.h \
    $${PWD}/OAIBook.h \
    $${PWD}/OAIPublisher.h \
    $${PWD}/OAIPublisher_books_inner.h \
    $${PWD}/OAISubject.h \
# APIs
    $${PWD}/OAIAuthorApi.h \
    $${PWD}/OAIBookApi.h \
    $${PWD}/OAIPublisherApi.h \
    $${PWD}/OAISearchApi.h \
    $${PWD}/OAIStatsApi.h \
    $${PWD}/OAISubjectApi.h \
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
    $${PWD}/OAIAuthor.cpp \
    $${PWD}/OAIAuthorQueryResults.cpp \
    $${PWD}/OAIBook.cpp \
    $${PWD}/OAIPublisher.cpp \
    $${PWD}/OAIPublisher_books_inner.cpp \
    $${PWD}/OAISubject.cpp \
# APIs
    $${PWD}/OAIAuthorApi.cpp \
    $${PWD}/OAIBookApi.cpp \
    $${PWD}/OAIPublisherApi.cpp \
    $${PWD}/OAISearchApi.cpp \
    $${PWD}/OAIStatsApi.cpp \
    $${PWD}/OAISubjectApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
