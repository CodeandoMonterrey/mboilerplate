"""
Using redirect route instead of simple routes since it supports strict_slash
Simple route: http://webapp-improved.appspot.com/guide/routing.html#simple-routes
RedirectRoute: http://webapp-improved.appspot.com/api/webapp2_extras/routes.html#webapp2_extras.routes.RedirectRoute
"""
from webapp2_extras.routes import RedirectRoute
from bp_includes import handlers as handlers

secure_scheme = 'https'

_routes = [
    RedirectRoute('/_ah/login_required', handlers.LoginRequiredHandler),
    

    # Landing
    RedirectRoute('/', handlers.MaterializeLandingRequestHandler, name='landing', strict_slash=True),   
    RedirectRoute('/blog/', handlers.MaterializeLandingBlogRequestHandler, name='blog', strict_slash=True),
    RedirectRoute('/blog/<post_id>/', handlers.MaterializeLandingBlogPostRequestHandler, name='blog-post', strict_slash=True),
    RedirectRoute('/contact/', handlers.MaterializeLandingContactRequestHandler, name='contact', strict_slash=True),
    RedirectRoute('/faq/', handlers.MaterializeLandingFaqRequestHandler, name='faq', strict_slash=True),
    RedirectRoute('/tou/', handlers.MaterializeLandingTouRequestHandler, name='tou', strict_slash=True),
    RedirectRoute('/privacy/', handlers.MaterializeLandingPrivacyRequestHandler, name='privacy', strict_slash=True),
    RedirectRoute('/license/', handlers.MaterializeLandingLicenseRequestHandler, name='license', strict_slash=True),
    RedirectRoute('/register/', handlers.MaterializeRegisterRequestHandler, name='register', strict_slash=True),
    RedirectRoute('/activation/<user_id>/<token>', handlers.MaterializeAccountActivationHandler, name='account-activation', strict_slash=True),
    RedirectRoute('/resend/<user_id>/<token>', handlers.ResendActivationEmailHandler, name='resend-account-activation', strict_slash=True),
    RedirectRoute('/register/referral/<user_id>/', handlers.MaterializeRegisterReferralHandler, name='register-referral', strict_slash=True),
    RedirectRoute('/activation/<ref_user_id>/<token>/<user_id>', handlers.MaterializeAccountActivationReferralHandler, name='account-activation-referral', strict_slash=True),
    #RedirectRoute('/resend/<ref_user_id>/<token>/<user_id>', handlers.ResendActivationEmailReferralHandler, name='resend-account-activation-referral', strict_slash=True),
    RedirectRoute('/login/', handlers.MaterializeLoginRequestHandler, name='login', strict_slash=True),
    RedirectRoute('/logout/', handlers.MaterializeLogoutRequestHandler, name='logout', strict_slash=True),
    RedirectRoute('/password-reset/', handlers.PasswordResetHandler, name='password-reset', strict_slash=True),
    RedirectRoute('/password-reset/<user_id>/<token>', handlers.PasswordResetCompleteHandler, name='password-reset-check', strict_slash=True),
    
    # User
    RedirectRoute('/user/home/', handlers.MaterializeHomeRequestHandler, name='materialize-home', strict_slash=True),
    RedirectRoute('/user/referrals/', handlers.MaterializeReferralsRequestHandler, name='materialize-referrals', strict_slash=True),
    RedirectRoute('/user/polymer/', handlers.MaterializePolymerRequestHandler, name='materialize-polymer', strict_slash=True),
    RedirectRoute('/user/cartodb/', handlers.MaterializeCartoDBRequestHandler, name='materialize-cartodb', strict_slash=True),
    RedirectRoute('/user/settings/profile/', handlers.MaterializeSettingsProfileRequestHandler, name='materialize-settings-profile', strict_slash=True),
    RedirectRoute('/user/settings/email/', handlers.MaterializeSettingsEmailRequestHandler, name='materialize-settings-email', strict_slash=True),
    RedirectRoute('/user/settings/password/', handlers.MaterializeSettingsPasswordRequestHandler, name='materialize-settings-password', strict_slash=True),
    RedirectRoute('/user/settings/delete/', handlers.MaterializeSettingsDeleteRequestHandler, name='materialize-settings-delete', strict_slash=True),
    RedirectRoute('/user/settings/referrals/', handlers.MaterializeSettingsReferralsRequestHandler, name='materialize-settings-referrals', strict_slash=True),
    RedirectRoute('/user/settings/account/', handlers.MaterializeSettingsAccountRequestHandler, name='materialize-settings-account', strict_slash=True),
    RedirectRoute('/user/change-email/<user_id>/<encoded_email>/<token>', handlers.MaterializeEmailChangedCompleteHandler, name='materialize-email-changed-check', strict_slash=True),
    
    # Statics
    RedirectRoute(r'/robots.txt', handlers.RobotsHandler, name='robots', strict_slash=True),
    RedirectRoute(r'/humans.txt', handlers.HumansHandler, name='humans', strict_slash=True),
    RedirectRoute(r'/sitemap.xml', handlers.SitemapHandler, name='sitemap', strict_slash=True),
    RedirectRoute(r'/crossdomain.xml', handlers.CrossDomainHandler, name='crossdomain', strict_slash=True),
    
    #Cronjobs
    RedirectRoute('/cronjob-welcome/', handlers.WelcomeCronjobHandler, name='cronjob-welcome', strict_slash=True),  
    
    #Taskqueues
    RedirectRoute('/taskqueue-send-email/', handlers.SendEmailHandler, name='taskqueue-send-email', strict_slash=True),
    RedirectRoute('/taskqueue-welcome/', handlers.WelcomeHandler, name='taskqueue-welcome', strict_slash=True),

    #API
    RedirectRoute('/mbapi/in/', handlers.APIIncomingHandler, name='mbapi-in', strict_slash=True),
    RedirectRoute('/mbapi/out/', handlers.APIOutgoingHandler, name='mbapi-out', strict_slash=True),
    RedirectRoute('/mbapi/test/', handlers.APITestingHandler, name='mbapi-test', strict_slash=True),

    # Blob handlers for small media
    RedirectRoute('/media/serve/<kind>/<media_id>/', handlers.MediaDownloadHandler, name='media-serve', strict_slash=True),
    # Blob handlers for large media
    RedirectRoute('/blobstore/form/', handlers.BlobFormHandler, name='blob-form', strict_slash=True),
    RedirectRoute('/blobstore/upload/', handlers.BlobUploadHandler, name='blob-upload', strict_slash=True),
    RedirectRoute('/blobstore/serve/<photo_key>', handlers.BlobDownloadHandler, name='blob-serve', strict_slash=True),
    
]

def get_routes():
    return _routes

def add_routes(app):
    if app.debug:
        secure_scheme = 'http'
    for r in _routes:
        app.router.add(r)
