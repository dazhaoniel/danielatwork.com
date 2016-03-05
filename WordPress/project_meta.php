<?php
// tutorial: https://www.smashingmagazine.com/2011/10/create-custom-post-meta-boxes-wordpress/
/* Fire our meta box setup function on the post editor screen. */
add_action( 'load-post.php', 'pilot_fish_project_meta_boxes_setup' );
add_action( 'load-post-new.php', 'pilot_fish_project_meta_boxes_setup' );

/* Meta box setup function. */
function pilot_fish_project_meta_boxes_setup() {
  /* Add meta boxes on the 'add_meta_boxes' hook. */
  add_action( 'add_meta_boxes', 'pilot_fish_add_project_meta_boxes' );

  /* Save post meta on the 'save_post' hook. */
  add_action( 'save_post', 'pilot_fish_save_project_meta', 10, 2 );
}

/* Create one or more meta boxes to be displayed on the post editor screen. */
function pilot_fish_add_project_meta_boxes() {

  add_meta_box(
    'pilot-fish-project-external-url',      // Unique ID
    esc_html__( 'External URL', 'pilot-fish' ),    // Title
    'pilot_fish_project_external_url_meta_box',   // Callback function
    'project',         // Admin page (or post type)
    'side',         // Context
    'default'         // Priority
  );
}

/* Display the post meta box. */
function pilot_fish_project_external_url_meta_box( $object, $box ) { ?>

  <?php wp_nonce_field( basename( __FILE__ ), 'pilot_fish_project_external_url_nonce' ); ?>

  <p>
    <label for="pilot-fish-project-external-url"><?php _e( "Add An External URL To Project.", 'pilot-fish' ); ?></label>
    <br />
    <input class="widefat" type="text" name="pilot-fish-project-external-url" id="pilot-fish-project-external-url" value="<?php echo esc_attr( get_post_meta( $object->ID, 'pilot-fish-project-external-url', true ) ); ?>" size="30" />
  </p>
<?php }

/* Save the meta box's post metadata. */
function pilot_fish_save_project_meta( $post_id, $post ) {

  /* Verify the nonce before proceeding. */
  if ( !isset( $_POST['pilot_fish_project_external_url_nonce'] ) || !wp_verify_nonce( $_POST['pilot_fish_project_external_url_nonce'], basename( __FILE__ ) ) )
    return $post_id;

  /* Get the post type object. */
  $post_type = get_post_type_object( $post->post_type );

  /* Check if the current user has permission to edit the post. */
  if ( !current_user_can( $post_type->cap->edit_post, $post_id ) )
    return $post_id;

  /* Get the posted data and sanitize it for use as an HTML class. */
  $new_meta_value = ( isset( $_POST['pilot-fish-project-external-url'] ) ? sanitize_html_class( $_POST['pilot-fish-project-external-url'] ) : '' );

  /* Get the meta key. */
  $meta_key = 'pilot-fish-project-external-url';

  /* Get the meta value of the custom field key. */
  $meta_value = get_post_meta( $post_id, $meta_key, true );

  /* If a new meta value was added and there was no previous value, add it. */
  if ( $new_meta_value && '' == $meta_value )
    add_post_meta( $post_id, $meta_key, $new_meta_value, true );

  /* If the new meta value does not match the old value, update it. */
  elseif ( $new_meta_value && $new_meta_value != $meta_value )
    update_post_meta( $post_id, $meta_key, $new_meta_value );

  /* If there is no new meta value but an old value exists, delete it. */
  elseif ( '' == $new_meta_value && $meta_value )
    delete_post_meta( $post_id, $meta_key, $meta_value );
}

?>