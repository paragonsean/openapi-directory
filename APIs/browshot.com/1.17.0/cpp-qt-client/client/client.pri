QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount.h \
    $${PWD}/OAIAccountError.h \
    $${PWD}/OAIBatch.h \
    $${PWD}/OAIBatchError.h \
    $${PWD}/OAIBrowser.h \
    $${PWD}/OAIBrowserError.h \
    $${PWD}/OAIBrowserList.h \
    $${PWD}/OAIInstance.h \
    $${PWD}/OAIInstanceError.h \
    $${PWD}/OAIInstanceList.h \
    $${PWD}/OAIScreenshot.h \
    $${PWD}/OAIScreenshotError.h \
    $${PWD}/OAIScreenshotHost.h \
    $${PWD}/OAIScreenshotInfoError.h \
    $${PWD}/OAIScreenshotList.h \
    $${PWD}/OAIScreenshotShort.h \
# APIs
    $${PWD}/OAIAccountApi.h \
    $${PWD}/OAIBatchApi.h \
    $${PWD}/OAIBrowserApi.h \
    $${PWD}/OAIInstanceApi.h \
    $${PWD}/OAIScreenshotApi.h \
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
    $${PWD}/OAIAccount.cpp \
    $${PWD}/OAIAccountError.cpp \
    $${PWD}/OAIBatch.cpp \
    $${PWD}/OAIBatchError.cpp \
    $${PWD}/OAIBrowser.cpp \
    $${PWD}/OAIBrowserError.cpp \
    $${PWD}/OAIBrowserList.cpp \
    $${PWD}/OAIInstance.cpp \
    $${PWD}/OAIInstanceError.cpp \
    $${PWD}/OAIInstanceList.cpp \
    $${PWD}/OAIScreenshot.cpp \
    $${PWD}/OAIScreenshotError.cpp \
    $${PWD}/OAIScreenshotHost.cpp \
    $${PWD}/OAIScreenshotInfoError.cpp \
    $${PWD}/OAIScreenshotList.cpp \
    $${PWD}/OAIScreenshotShort.cpp \
# APIs
    $${PWD}/OAIAccountApi.cpp \
    $${PWD}/OAIBatchApi.cpp \
    $${PWD}/OAIBrowserApi.cpp \
    $${PWD}/OAIInstanceApi.cpp \
    $${PWD}/OAIScreenshotApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
