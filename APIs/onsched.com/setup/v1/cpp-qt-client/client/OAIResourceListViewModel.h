/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIResourceListViewModel.h
 *
 * 
 */

#ifndef OAIResourceListViewModel_H
#define OAIResourceListViewModel_H

#include <QJsonObject>

#include "OAIResourceViewModel.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIResourceViewModel;

class OAIResourceListViewModel : public OAIObject {
public:
    OAIResourceListViewModel();
    OAIResourceListViewModel(QString json);
    ~OAIResourceListViewModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCount() const;
    void setCount(const qint32 &count);
    bool is_count_Set() const;
    bool is_count_Valid() const;

    QList<OAIResourceViewModel> getData() const;
    void setData(const QList<OAIResourceViewModel> &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    bool isHasMore() const;
    void setHasMore(const bool &has_more);
    bool is_has_more_Set() const;
    bool is_has_more_Valid() const;

    QString getObject() const;
    void setObject(const QString &object);
    bool is_object_Set() const;
    bool is_object_Valid() const;

    qint32 getTotal() const;
    void setTotal(const qint32 &total);
    bool is_total_Set() const;
    bool is_total_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_count;
    bool m_count_isSet;
    bool m_count_isValid;

    QList<OAIResourceViewModel> m_data;
    bool m_data_isSet;
    bool m_data_isValid;

    bool m_has_more;
    bool m_has_more_isSet;
    bool m_has_more_isValid;

    QString m_object;
    bool m_object_isSet;
    bool m_object_isValid;

    qint32 m_total;
    bool m_total_isSet;
    bool m_total_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIResourceListViewModel)

#endif // OAIResourceListViewModel_H
