QT += network

HEADERS += \
# Models
    $${PWD}/OAIArc.h \
    $${PWD}/OAIDependenciesOut.h \
    $${PWD}/OAIEntitiesOut.h \
    $${PWD}/OAIEntityOut.h \
    $${PWD}/OAIHTTPValidationError.h \
    $${PWD}/OAISentenceDependenciesOut.h \
    $${PWD}/OAISentenceDependencyOut.h \
    $${PWD}/OAIUserRequestIn.h \
    $${PWD}/OAIValidationError.h \
    $${PWD}/OAIVersionOut.h \
    $${PWD}/OAIWord.h \
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
    $${PWD}/OAIArc.cpp \
    $${PWD}/OAIDependenciesOut.cpp \
    $${PWD}/OAIEntitiesOut.cpp \
    $${PWD}/OAIEntityOut.cpp \
    $${PWD}/OAIHTTPValidationError.cpp \
    $${PWD}/OAISentenceDependenciesOut.cpp \
    $${PWD}/OAISentenceDependencyOut.cpp \
    $${PWD}/OAIUserRequestIn.cpp \
    $${PWD}/OAIValidationError.cpp \
    $${PWD}/OAIVersionOut.cpp \
    $${PWD}/OAIWord.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
