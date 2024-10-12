QT += network

HEADERS += \
# Models
    $${PWD}/OAIArrayOfBatch.h \
    $${PWD}/OAIBatch.h \
    $${PWD}/OAICheckDomain_200_response.h \
    $${PWD}/OAICreateBatch_request.h \
    $${PWD}/OAICreateBatch_request_options.h \
    $${PWD}/OAIDomainRank_200_response.h \
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
    $${PWD}/OAIArrayOfBatch.cpp \
    $${PWD}/OAIBatch.cpp \
    $${PWD}/OAICheckDomain_200_response.cpp \
    $${PWD}/OAICreateBatch_request.cpp \
    $${PWD}/OAICreateBatch_request_options.cpp \
    $${PWD}/OAIDomainRank_200_response.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
