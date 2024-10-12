QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorFieldContract.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIWorkbook.h \
    $${PWD}/OAIWorkbookError.h \
    $${PWD}/OAIWorkbookProperties.h \
    $${PWD}/OAIWorkbookPropertiesUpdateParameters.h \
    $${PWD}/OAIWorkbookUpdateParameters.h \
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
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIWorkbook.cpp \
    $${PWD}/OAIWorkbookError.cpp \
    $${PWD}/OAIWorkbookProperties.cpp \
    $${PWD}/OAIWorkbookPropertiesUpdateParameters.cpp \
    $${PWD}/OAIWorkbookUpdateParameters.cpp \
    $${PWD}/OAIWorkbooksListResult.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
