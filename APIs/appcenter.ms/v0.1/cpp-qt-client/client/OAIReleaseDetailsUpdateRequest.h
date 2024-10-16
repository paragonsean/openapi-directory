/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIReleaseDetailsUpdateRequest.h
 *
 * A request containing information for updating details of a release
 */

#ifndef OAIReleaseDetailsUpdateRequest_H
#define OAIReleaseDetailsUpdateRequest_H

#include <QJsonObject>

#include "OAIReleases_getLatestByDistributionGroup_200_response_build.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIReleases_getLatestByDistributionGroup_200_response_build;

class OAIReleaseDetailsUpdateRequest : public OAIObject {
public:
    OAIReleaseDetailsUpdateRequest();
    OAIReleaseDetailsUpdateRequest(QString json);
    ~OAIReleaseDetailsUpdateRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIReleases_getLatestByDistributionGroup_200_response_build getBuild() const;
    void setBuild(const OAIReleases_getLatestByDistributionGroup_200_response_build &build);
    bool is_build_Set() const;
    bool is_build_Valid() const;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    QString getReleaseNotes() const;
    void setReleaseNotes(const QString &release_notes);
    bool is_release_notes_Set() const;
    bool is_release_notes_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIReleases_getLatestByDistributionGroup_200_response_build m_build;
    bool m_build_isSet;
    bool m_build_isValid;

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;

    QString m_release_notes;
    bool m_release_notes_isSet;
    bool m_release_notes_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIReleaseDetailsUpdateRequest)

#endif // OAIReleaseDetailsUpdateRequest_H
