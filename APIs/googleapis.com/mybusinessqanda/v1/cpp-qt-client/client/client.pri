QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnswer.h \
    $${PWD}/OAIAuthor.h \
    $${PWD}/OAIListAnswersResponse.h \
    $${PWD}/OAIListQuestionsResponse.h \
    $${PWD}/OAIQuestion.h \
    $${PWD}/OAIUpsertAnswerRequest.h \
# APIs
    $${PWD}/OAILocationsApi.h \
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
    $${PWD}/OAIAnswer.cpp \
    $${PWD}/OAIAuthor.cpp \
    $${PWD}/OAIListAnswersResponse.cpp \
    $${PWD}/OAIListQuestionsResponse.cpp \
    $${PWD}/OAIQuestion.cpp \
    $${PWD}/OAIUpsertAnswerRequest.cpp \
# APIs
    $${PWD}/OAILocationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
