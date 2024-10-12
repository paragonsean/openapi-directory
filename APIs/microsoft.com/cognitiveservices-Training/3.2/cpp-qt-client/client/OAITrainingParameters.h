/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITrainingParameters.h
 *
 * Parameters used for training.
 */

#ifndef OAITrainingParameters_H
#define OAITrainingParameters_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITrainingParameters : public OAIObject {
public:
    OAITrainingParameters();
    OAITrainingParameters(QString json);
    ~OAITrainingParameters() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getSelectedTags() const;
    void setSelectedTags(const QList<QString> &selected_tags);
    bool is_selected_tags_Set() const;
    bool is_selected_tags_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_selected_tags;
    bool m_selected_tags_isSet;
    bool m_selected_tags_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITrainingParameters)

#endif // OAITrainingParameters_H
