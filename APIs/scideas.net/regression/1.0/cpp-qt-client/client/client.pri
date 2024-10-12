QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIInline_response_200.h \
    $${PWD}/OAIRegression_api_body.h \
    $${PWD}/OAIResult.h \
    $${PWD}/OAIResult_calls.h \
    $${PWD}/OAIResult_standardized_coefficients.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIInline_response_200.cpp \
    $${PWD}/OAIRegression_api_body.cpp \
    $${PWD}/OAIResult.cpp \
    $${PWD}/OAIResult_calls.cpp \
    $${PWD}/OAIResult_standardized_coefficients.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
