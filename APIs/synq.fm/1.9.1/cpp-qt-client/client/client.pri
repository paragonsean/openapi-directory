QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorObject.h \
    $${PWD}/OAIStreamConfigurationObject.h \
    $${PWD}/OAIStreamInformationObject.h \
    $${PWD}/OAIUploadParameterObject.h \
    $${PWD}/OAIUploaderInformationObject.h \
    $${PWD}/OAIVideoObject.h \
# APIs
    $${PWD}/OAIVideoApi.h \
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
    $${PWD}/OAIErrorObject.cpp \
    $${PWD}/OAIStreamConfigurationObject.cpp \
    $${PWD}/OAIStreamInformationObject.cpp \
    $${PWD}/OAIUploadParameterObject.cpp \
    $${PWD}/OAIUploaderInformationObject.cpp \
    $${PWD}/OAIVideoObject.cpp \
# APIs
    $${PWD}/OAIVideoApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
