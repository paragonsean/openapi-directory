QT += network

HEADERS += \
# Models
    $${PWD}/OAIBoard.h \
    $${PWD}/OAIBoardResponse.h \
    $${PWD}/OAIErrorModel.h \
    $${PWD}/OAIJourneyResponse.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAILocationResponse.h \
    $${PWD}/OAITrainLocation.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIBoard.cpp \
    $${PWD}/OAIBoardResponse.cpp \
    $${PWD}/OAIErrorModel.cpp \
    $${PWD}/OAIJourneyResponse.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAILocationResponse.cpp \
    $${PWD}/OAITrainLocation.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
