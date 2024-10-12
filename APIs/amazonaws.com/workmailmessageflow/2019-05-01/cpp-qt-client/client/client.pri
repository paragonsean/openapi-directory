QT += network

HEADERS += \
# Models
    $${PWD}/OAIGetRawMessageContentResponse.h \
    $${PWD}/OAIPutRawMessageContentRequest.h \
    $${PWD}/OAIPutRawMessageContentRequest_content.h \
    $${PWD}/OAIPutRawMessageContent_request.h \
    $${PWD}/OAIPutRawMessageContent_request_content.h \
    $${PWD}/OAIPutRawMessageContent_request_content_s3Reference.h \
    $${PWD}/OAIRawMessageContent.h \
    $${PWD}/OAIS3Reference.h \
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
    $${PWD}/OAIGetRawMessageContentResponse.cpp \
    $${PWD}/OAIPutRawMessageContentRequest.cpp \
    $${PWD}/OAIPutRawMessageContentRequest_content.cpp \
    $${PWD}/OAIPutRawMessageContent_request.cpp \
    $${PWD}/OAIPutRawMessageContent_request_content.cpp \
    $${PWD}/OAIPutRawMessageContent_request_content_s3Reference.cpp \
    $${PWD}/OAIRawMessageContent.cpp \
    $${PWD}/OAIS3Reference.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
