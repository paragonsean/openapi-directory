QT += network

HEADERS += \
# Models
    $${PWD}/OAIAPI401Response.h \
    $${PWD}/OAIAPI404Response.h \
    $${PWD}/OAIFeed.h \
    $${PWD}/OAIFeedVersion.h \
    $${PWD}/OAIFeedVersionIssue.h \
    $${PWD}/OAIFeedVersion_d.h \
    $${PWD}/OAIFeed_latest.h \
    $${PWD}/OAIFeed_u.h \
    $${PWD}/OAIGetFeedVersionsResponse.h \
    $${PWD}/OAIGetFeedVersionsResponse_results.h \
    $${PWD}/OAIGetFeedsResponse.h \
    $${PWD}/OAIGetFeedsResponse_results.h \
    $${PWD}/OAIGetLatestFeedVersionResponse.h \
    $${PWD}/OAIGetLocationsResponse.h \
    $${PWD}/OAIGetLocationsResponse_results.h \
    $${PWD}/OAILocation.h \
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
    $${PWD}/OAIAPI401Response.cpp \
    $${PWD}/OAIAPI404Response.cpp \
    $${PWD}/OAIFeed.cpp \
    $${PWD}/OAIFeedVersion.cpp \
    $${PWD}/OAIFeedVersionIssue.cpp \
    $${PWD}/OAIFeedVersion_d.cpp \
    $${PWD}/OAIFeed_latest.cpp \
    $${PWD}/OAIFeed_u.cpp \
    $${PWD}/OAIGetFeedVersionsResponse.cpp \
    $${PWD}/OAIGetFeedVersionsResponse_results.cpp \
    $${PWD}/OAIGetFeedsResponse.cpp \
    $${PWD}/OAIGetFeedsResponse_results.cpp \
    $${PWD}/OAIGetLatestFeedVersionResponse.cpp \
    $${PWD}/OAIGetLocationsResponse.cpp \
    $${PWD}/OAIGetLocationsResponse_results.cpp \
    $${PWD}/OAILocation.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
