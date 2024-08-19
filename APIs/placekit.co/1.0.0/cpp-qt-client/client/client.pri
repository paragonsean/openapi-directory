QT += network

HEADERS += \
# Models
    $${PWD}/OAIEntity.h \
    $${PWD}/OAIParameters.h \
    $${PWD}/OAIResults.h \
    $${PWD}/OAIReverse_request.h \
    $${PWD}/OAISearch_request.h \
    $${PWD}/OAITypes.h \
    $${PWD}/OAIValidationError.h \
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
    $${PWD}/OAIEntity.cpp \
    $${PWD}/OAIParameters.cpp \
    $${PWD}/OAIResults.cpp \
    $${PWD}/OAIReverse_request.cpp \
    $${PWD}/OAISearch_request.cpp \
    $${PWD}/OAITypes.cpp \
    $${PWD}/OAIValidationError.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
