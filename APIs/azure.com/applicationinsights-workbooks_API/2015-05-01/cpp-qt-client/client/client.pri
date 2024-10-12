QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorFieldContract.h \
    $${PWD}/OAILinkProperties.h \
    $${PWD}/OAIWorkbook.h \
    $${PWD}/OAIWorkbookError.h \
    $${PWD}/OAIWorkbookProperties.h \
    $${PWD}/OAIWorkbookResource.h \
    $${PWD}/OAIWorkbooksListResult.h \
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
    $${PWD}/OAIErrorFieldContract.cpp \
    $${PWD}/OAILinkProperties.cpp \
    $${PWD}/OAIWorkbook.cpp \
    $${PWD}/OAIWorkbookError.cpp \
    $${PWD}/OAIWorkbookProperties.cpp \
    $${PWD}/OAIWorkbookResource.cpp \
    $${PWD}/OAIWorkbooksListResult.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
