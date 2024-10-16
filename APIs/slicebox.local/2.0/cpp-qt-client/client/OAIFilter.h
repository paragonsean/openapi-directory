/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFilter.h
 *
 * 
 */

#ifndef OAIFilter_H
#define OAIFilter_H

#include <QJsonObject>

#include "OAITagPathTag.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITagPathTag;

class OAIFilter : public OAIObject {
public:
    OAIFilter();
    OAIFilter(QString json);
    ~OAIFilter() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getTagFilterType() const;
    void setTagFilterType(const QString &tag_filter_type);
    bool is_tag_filter_type_Set() const;
    bool is_tag_filter_type_Valid() const;

    QList<OAITagPathTag> getTags() const;
    void setTags(const QList<OAITagPathTag> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_tag_filter_type;
    bool m_tag_filter_type_isSet;
    bool m_tag_filter_type_isValid;

    QList<OAITagPathTag> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFilter)

#endif // OAIFilter_H
