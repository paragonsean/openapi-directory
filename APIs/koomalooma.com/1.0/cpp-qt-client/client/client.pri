QT += network

HEADERS += \
# Models
    $${PWD}/OAICommitment.h \
    $${PWD}/OAICommitmentRequest.h \
    $${PWD}/OAIGoal.h \
    $${PWD}/OAIUser.h \
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
    $${PWD}/OAICommitment.cpp \
    $${PWD}/OAICommitmentRequest.cpp \
    $${PWD}/OAIGoal.cpp \
    $${PWD}/OAIUser.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
