QT += network

HEADERS += \
# Models
    $${PWD}/OAIAttendance.h \
    $${PWD}/OAIAttendee.h \
    $${PWD}/OAIDateTimeRange.h \
    $${PWD}/OAIHostUrl.h \
    $${PWD}/OAINotifiedParties.h \
    $${PWD}/OAIOrganizer.h \
    $${PWD}/OAIRecording.h \
    $${PWD}/OAIRecordingsListForTraining.h \
    $${PWD}/OAIRegistrant.h \
    $${PWD}/OAIRegistrantCreated.h \
    $${PWD}/OAIRegistrantReqCreate.h \
    $${PWD}/OAIRegistrationSettings.h \
    $${PWD}/OAISession.h \
    $${PWD}/OAITraining.h \
    $${PWD}/OAITrainingNameDescription.h \
    $${PWD}/OAITrainingOrganizers.h \
    $${PWD}/OAITrainingReqCreate.h \
    $${PWD}/OAITrainingTimes.h \
# APIs
    $${PWD}/OAIOrganizersApi.h \
    $${PWD}/OAIRecordingsApi.h \
    $${PWD}/OAIRegistrationsApi.h \
    $${PWD}/OAIReportsApi.h \
    $${PWD}/OAITrainingsApi.h \
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
    $${PWD}/OAIAttendance.cpp \
    $${PWD}/OAIAttendee.cpp \
    $${PWD}/OAIDateTimeRange.cpp \
    $${PWD}/OAIHostUrl.cpp \
    $${PWD}/OAINotifiedParties.cpp \
    $${PWD}/OAIOrganizer.cpp \
    $${PWD}/OAIRecording.cpp \
    $${PWD}/OAIRecordingsListForTraining.cpp \
    $${PWD}/OAIRegistrant.cpp \
    $${PWD}/OAIRegistrantCreated.cpp \
    $${PWD}/OAIRegistrantReqCreate.cpp \
    $${PWD}/OAIRegistrationSettings.cpp \
    $${PWD}/OAISession.cpp \
    $${PWD}/OAITraining.cpp \
    $${PWD}/OAITrainingNameDescription.cpp \
    $${PWD}/OAITrainingOrganizers.cpp \
    $${PWD}/OAITrainingReqCreate.cpp \
    $${PWD}/OAITrainingTimes.cpp \
# APIs
    $${PWD}/OAIOrganizersApi.cpp \
    $${PWD}/OAIRecordingsApi.cpp \
    $${PWD}/OAIRegistrationsApi.cpp \
    $${PWD}/OAIReportsApi.cpp \
    $${PWD}/OAITrainingsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
