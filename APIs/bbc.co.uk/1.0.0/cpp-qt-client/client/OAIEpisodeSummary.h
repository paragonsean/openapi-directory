/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEpisodeSummary.h
 *
 * 
 */

#ifndef OAIEpisodeSummary_H
#define OAIEpisodeSummary_H

#include <QJsonObject>

#include "OAIAncestorSummary.h"
#include "OAIAvailableVersions.h"
#include "OAIImage.h"
#include "OAINetworkSummary.h"
#include "OAIProgrammeTitles.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAncestorSummary;
class OAIAvailableVersions;
class OAIImage;
class OAINetworkSummary;
class OAIProgrammeTitles;

class OAIEpisodeSummary : public OAIObject {
public:
    OAIEpisodeSummary();
    OAIEpisodeSummary(QString json);
    ~OAIEpisodeSummary() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIAncestorSummary> getAncestors() const;
    void setAncestors(const QList<OAIAncestorSummary> &ancestors);
    bool is_ancestors_Set() const;
    bool is_ancestors_Valid() const;

    QList<OAIAvailableVersions> getAvailableVersions() const;
    void setAvailableVersions(const QList<OAIAvailableVersions> &available_versions);
    bool is_available_versions_Set() const;
    bool is_available_versions_Valid() const;

    QList<OAIImage> getImages() const;
    void setImages(const QList<OAIImage> &images);
    bool is_images_Set() const;
    bool is_images_Valid() const;

    QString getMediaType() const;
    void setMediaType(const QString &media_type);
    bool is_media_type_Set() const;
    bool is_media_type_Valid() const;

    OAINetworkSummary getNetworkSummary() const;
    void setNetworkSummary(const OAINetworkSummary &network_summary);
    bool is_network_summary_Set() const;
    bool is_network_summary_Valid() const;

    QString getPid() const;
    void setPid(const QString &pid);
    bool is_pid_Set() const;
    bool is_pid_Valid() const;

    QString getReleaseDate() const;
    void setReleaseDate(const QString &release_date);
    bool is_release_date_Set() const;
    bool is_release_date_Valid() const;

    QString getShortSynopsis() const;
    void setShortSynopsis(const QString &short_synopsis);
    bool is_short_synopsis_Set() const;
    bool is_short_synopsis_Valid() const;

    OAIProgrammeTitles getTitles() const;
    void setTitles(const OAIProgrammeTitles &titles);
    bool is_titles_Set() const;
    bool is_titles_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIAncestorSummary> m_ancestors;
    bool m_ancestors_isSet;
    bool m_ancestors_isValid;

    QList<OAIAvailableVersions> m_available_versions;
    bool m_available_versions_isSet;
    bool m_available_versions_isValid;

    QList<OAIImage> m_images;
    bool m_images_isSet;
    bool m_images_isValid;

    QString m_media_type;
    bool m_media_type_isSet;
    bool m_media_type_isValid;

    OAINetworkSummary m_network_summary;
    bool m_network_summary_isSet;
    bool m_network_summary_isValid;

    QString m_pid;
    bool m_pid_isSet;
    bool m_pid_isValid;

    QString m_release_date;
    bool m_release_date_isSet;
    bool m_release_date_isValid;

    QString m_short_synopsis;
    bool m_short_synopsis_isSet;
    bool m_short_synopsis_isValid;

    OAIProgrammeTitles m_titles;
    bool m_titles_isSet;
    bool m_titles_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEpisodeSummary)

#endif // OAIEpisodeSummary_H
